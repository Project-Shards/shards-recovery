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
from shard_updater.widgets.MenuButton import MenuButton

@Gtk.Template(resource_path='/al/getcryst/shard/updater/windows/InstallWindow.ui')
class InstallWindow(Adw.Bin):
    __gtype_name__ = 'InstallWindow'

    Disk_select = Gtk.Template.Child()
    carousel = Gtk.Template.Child()

    def __init__(self, window, headerbar, **kwargs):
        super().__init__(**kwargs)
        self.window = window
        self.headerbar = headerbar
        self.headerbar.set_title("Install Project Shards")
        self.headerbar.remove_all_buttons()
        button = MenuButton(label="Quit Installer", on_clicked=self.on_quit_button_clicked)
        self.headerbar.add_button(button)

    def on_quit_button_clicked(self, button):
        self.window.switch_to_main()
