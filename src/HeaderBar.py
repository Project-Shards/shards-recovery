# HeaderBar.py
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

from gi.repository import Adw, Gtk

@Gtk.Template(resource_path='/al/getcryst/shard/updater/HeaderBar.ui')
class HeaderBar(Gtk.Box):
    __gtype_name__ = "HeaderBar"

    title_text = Gtk.Template.Child()
    header_buttons = []

    def __init__(self, window, **kwargs):
        super().__init__(**kwargs)
        self.window = window

    def set_title(self, title):
        self.title_text.set_title(title)

    def add_button(self, button):
        print(button.label)
        self.header_buttons.append(button)
        self.append(button)
        print(self.header_buttons)

    def remove_all_buttons(self):
        for button in self.header_buttons:
            print("Remove "+button.label)
            self.remove(button)
        self.header_buttons = []
