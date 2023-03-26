# UpgradeWindow.py
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


from gi.repository import Gtk, GLib
from shard_updater.utils.threading import RunAsync
from shard_updater.windows.UpgradeWindows.Upgrade import Upgrade
from shard_updater.windows.UpgradeWindows.UpgradeFail import UpgradeFail
from shard_updater.windows.UpgradeWindows.UpgradeFinish import UpgradeFinish
from shard_updater.utils.threading import RunAsync
import math
import time

@Gtk.Template(resource_path='/al/getcryst/shard/updater/windows/UpgradeWindow.ui')
class UpgradeWindow(Gtk.Stack):
    __gtype_name__ = 'UpgradeWindow'

    upgrade = Gtk.Template.Child()
    upgradefinish = Gtk.Template.Child()
    upgradefail = Gtk.Template.Child()
    update_started = False

    def __init__(self, window, headerbar, **kwargs):
        super().__init__(**kwargs)
        self.window = window
        self.headerbar = headerbar
        self.upgrade.set_window(self)


    def resize(self, current_width, current_height, target_width, target_height):
        def resize_width(self, current_width, target_width):
            print("width")
            print("Current width: " + str(current_width))
            print("Target width: " + str(target_width))
            for i in range(current_width, target_width, -1 if current_width > target_width else 1):
                GLib.idle_add(self.set_margin_start, i)
                GLib.idle_add(self.set_margin_end, i)
                time.sleep(0.001)

        def resize_height(self, current_height, target_height):
            print("height")
            print("Target height: " + str(target_height))
            print("Current height: " + str(current_height))
            for i in range(current_height, target_height, -1 if current_height > target_height else 1):
                GLib.idle_add(self.set_margin_top, i-25)
                GLib.idle_add(self.set_margin_bottom, i)
                time.sleep(0.001)



        RunAsync(resize_width, None, self, current_width, target_width)
        RunAsync(resize_height, None, self, current_height, target_height)
        self.set_valign(Gtk.Align.FILL)
        self.set_halign(Gtk.Align.FILL)



    def upgrade_finished(self, success: bool):
        self.new_margin_height = math.ceil(((self.window.get_allocated_height() - self.allocated_height)*0.8) / 2)
        self.new_margin_width = math.ceil(((self.window.get_allocated_width() - self.allocated_width)*1) / 2)
        self.resize(self.margin_width, self.margin_height, self.new_margin_width, self.new_margin_height)
        if success:
            self.set_visible_child(self.upgradefinish)
            self.upgradefinish.on_show(
                self.headerbar,
                self,
                self.new_margin_width,
                self.new_margin_height
            )
        else:
            self.set_visible_child(self.upgradefail)
            self.upgradefail.on_show(
                self.headerbar,
                self,
                self.new_margin_width,
                self.new_margin_height
            )

    def on_show(self, allocated_width, allocated_height):
        self.allocated_width = allocated_width
        self.allocated_height = allocated_height
        self.margin_height = math.ceil(((self.window.get_allocated_height() - self.get_allocated_height())*0.2) / 2)
        self.margin_width = math.ceil(((self.window.get_allocated_width() - self.get_allocated_width())*0.5) / 2)
        self.current_margin_height = math.ceil((self.window.get_allocated_height() - self.allocated_height) / 2)
        self.current_margin_width = math.ceil((self.window.get_allocated_width() - self.allocated_width) / 2)

        self.resize(self.current_margin_width, self.current_margin_height, self.margin_width, self.margin_height)
        self.headerbar.set_title("Project Shards Updater")
        self.headerbar.remove_all_buttons()
        if not self.update_started:
            RunAsync(self.upgrade.root_step)
            self.update_started=True

    def on_quit_button_clicked(self, button):
        self.window.switch_to_main()
