# UpgradeFail.py
#
# Copyright 2023 axtlos <axtlos@getcryst.al>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License only.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0

from gi.repository import Gtk, Adw, GLib
import time
from shard_updater.widgets.MenuButton import MenuButton
from shard_updater.widgets.YNDialog import YNDialog
from shard_updater.windows.LogView import LogView
from shard_updater.utils.threading import RunAsync
import math
import subprocess

@Gtk.Template(resource_path='/al/getcryst/shard/updater/windows/UpgradeWindows/UpgradeFail.ui')
class UpgradeFail(Adw.Bin):
    __gtype_name__="UpgradeFail"

    button_reboot = Gtk.Template.Child()
    button_retry  = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.button = MenuButton(label="Return to Recovery", on_clicked=self.return_to_recovery)
        self.poweroff = MenuButton(label="Shut down Computer", on_clicked=self.poweroff)
        self.log = MenuButton(label="Show log", on_clicked=self.toggle_log)
        self.button_reboot.connect('clicked', self.reboot)
        self.button_retry.connect('clicked', self.retry)
        self.log_show = False
        self.log_window_upgradefail = LogView(logfile='/tmp/shardsrecovery.log')

    def retry(self, widget):
        self.return_to_recovery()
        # TODO: Retry upgrade

    def reboot(self, widget):
        def reboot_yes():
            subprocess.run(["reboot"])

        dialog = YNDialog(
            header="Reboot",
            body="Are you sure you want to reboot the computer?",
            yes_text="Reboot",
            no_text="Cancel",
            on_yes=reboot_yes,
            on_no=None,
            window=self.window.get_parent().get_parent().get_parent() # This is a hack to get the main window, but it works :shipit:
        )
        dialog.display()

    def poweroff(self, widget):
        def poweroff_yes():
            subprocess.run(["poweroff"])

        dialog = YNDialog(
            header="Power off",
            body="Are you sure you want to power off the computer?",
            yes_text="Power off",
            no_text="Cancel",
            on_yes=poweroff_yes,
            on_no=None,
            window=self.window.get_parent().get_parent().get_parent() # This is a hack to get the main window, but it works :shipit:
        )
        dialog.display()

    def animate_resize(self, targetwidth, targetheight, currentwidth, currentheight):
        def animate_height(self, targetheight, currentheight):
            for i in range(currentheight, targetheight, -2 if currentheight > targetheight else 2):
                if currentheight == targetheight:
                    break
                GLib.idle_add(self.window.set_margin_top, i)
                GLib.idle_add(self.window.set_margin_bottom, i)
                time.sleep(0.001)

        def animate_width(self, targetwidth, currentwidth):
            for i in range(currentwidth, targetwidth, -2 if currentwidth > targetwidth else 2):
                if currentwidth == targetwidth:
                    break
                GLib.idle_add(self.window.set_margin_start, i)
                GLib.idle_add(self.window.set_margin_end, i)
                time.sleep(0.001)
        RunAsync(animate_height, None, self, targetheight, currentheight)
        RunAsync(animate_width, None, self, targetwidth, currentwidth)

    def toggle_log(self, widget):
        print("Height "+str(self.window.get_allocated_height()))
        print("Width "+str(self.window.get_allocated_width()))
        if not self.log_show:
            self.window.set_transition_type(Gtk.StackTransitionType.CROSSFADE)
            self.window.set_visible_child(self.log_window_upgradefail)
            self.log_window_upgradefail.on_show()
            self.window.set_margin_start(self.widthmargin)
            self.window.set_margin_end(self.widthmargin)
            self.window.set_margin_top(self.heightmargin)
            self.window.set_margin_bottom(self.heightmargin)
            self.window.set_valign(Gtk.Align.FILL)
            self.window.set_halign(Gtk.Align.FILL)
            self.animate_resize(
                targetwidth=self.widthmargin,
                targetheight=self.heightmargin,
                currentwidth=self.widthmargin,
                currentheight=self.heightmargin
            )
            self.log_show = True
            self.window.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT)
        else:
            self.window.set_transition_type(Gtk.StackTransitionType.CROSSFADE)
            self.window.set_visible_child(self)
            self.animate_resize(
                targetwidth=self.orig_widthmargin,
                targetheight=self.orig_heightmargin,
                currentwidth=self.widthmargin,
                currentheight=self.heightmargin
            )
            self.log_show = False
            self.window.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT)

    def return_to_recovery(self, widget):
        self.window.on_quit_button_clicked(widget)

    def on_show(self, headerbar, window, curr_width_margin, curr_height_margin):
        self.headerbar = headerbar
        self.window = window
        self.window.add_child(self.log_window_upgradefail)
        self.heightmargin = math.ceil(curr_height_margin*0.5)
        self.widthmargin = math.ceil(curr_width_margin*0.5)
        self.orig_heightmargin = curr_height_margin
        self.orig_widthmargin = curr_width_margin
        self.headerbar.set_title("Project Shards Updater")
        self.headerbar.remove_all_buttons()
        self.headerbar.add_button(self.log)
        self.headerbar.add_button(self.button)
        self.headerbar.add_button(self.poweroff)
