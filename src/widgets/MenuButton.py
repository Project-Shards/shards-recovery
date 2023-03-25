# MenuButton.py
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

from gi.repository import Gtk

@Gtk.Template(resource_path='/al/getcryst/shard/updater/widgets/MenuButton.ui')
class MenuButton(Gtk.Button):
    __gtype_name__ = "MenuButton"

    def __init__(self, label, on_clicked, **kwargs):
        super().__init__(**kwargs)
        self.label = label
        self.set_label(self.label)
        self.connect("clicked", on_clicked)
