# InstallWindow.py
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

from gi.repository import Gtk, Adw
from shard_updater.windows.InstallWindows.DiskSelect import DiskSelect
from shard_updater.windows.InstallWindows.InstallProgress import InstallProgress
from shard_updater.windows.InstallWindows.InstallFinish import InstallFinish
from shard_updater.windows.InstallWindows.InstallFail import InstallFail
from shard_updater.widgets.MenuButton import MenuButton

@Gtk.Template(resource_path='/al/getcryst/shard/updater/windows/InstallWindow.ui')
class InstallWindow(Gtk.Stack):
    __gtype_name__ = 'InstallWindow'

    Disk_select = Gtk.Template.Child()
    Install_progress = Gtk.Template.Child()
    InstallFail = Gtk.Template.Child()
    InstallFinish = Gtk.Template.Child()

    def __init__(self, window, headerbar, **kwargs):
        super().__init__(**kwargs)
        self.window = window
        self.headerbar = headerbar
        self.button = MenuButton(label="Quit Installer", on_clicked=self.on_quit_button_clicked)
        self.Disk_select.continue_button.connect("clicked", self.on_disk_select_next_clicked)
        self.Install_progress.set_window(self)

    def on_show(self):
        self.headerbar.set_title("Install Project Shards")
        self.headerbar.remove_all_buttons()
        self.headerbar.add_button(self.button)

    def on_quit_button_clicked(self, button):
        self.window.switch_to_main()

    def on_install_finished(self, success: bool):
        print("Install finished: " + str(success))
        print("Window height "+ str( self.window.get_allocated_height()))
        print("Window width "+ str( self.window.get_allocated_width()))
        if not success:
            self.set_visible_child(self.InstallFail)
            self.InstallFail.on_show(self.headerbar, self, self.window.get_allocated_width(), self.window.get_allocated_height())
        else:
            self.set_visible_child(self.InstallFinish)
            self.InstallFinish.on_show(self.headerbar, self, self.window.get_allocated_width(), self.window.get_allocated_height())

    def on_disk_select_next_clicked(self, button):
        self.set_visible_child(self.Install_progress)
        self.headerbar.remove_all_buttons()
        self.Install_progress.on_show(self.Disk_select.selected_disk)
