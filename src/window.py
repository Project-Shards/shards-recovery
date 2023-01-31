# window.py
#
# Copyright 2023 Unknown
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw
from gi.repository import Gtk

@Gtk.Template(resource_path='/al/getcryst/shard/updater/window.ui')
class ShardUpdaterWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'ShardUpdaterWindow'

    #label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fullscreen()

        """
        .window {
	padding-left: 100px;
padding-right: 100px;
padding-top: 100px;
padding-bottom: 100px;
	background-color: #303030;
border-radius: 6px;
  box-shadow: 0 1px 4px 1px alpha(black, 0.13),
              0 1px 10px 5px alpha(black, 0.09),
              0 3px 16px 8px alpha(black, 0.04),
              0 0 0 1px alpha(black, .05);
}

        """
