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

from gi.repository import Gtk, Adw
from shard_updater.widgets.MenuButton import MenuButton

@Gtk.Template(resource_path='/al/getcryst/shard/updater/windows/UpgradeWindows/UpgradeFail.ui')
class UpgradeFail(Adw.Bin):
    __gtype_name__="UpgradeFail"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.button = MenuButton(label="Return to Recovery", on_clicked=self.enmpty)
        self.poweroff = MenuButton(label="Shut down Computer", on_clicked=self.enmpty)
        self.log = MenuButton(label="Show log", on_clicked=self.enmpty)

    def enmpty(self):
        pass

    def on_show(self, headerbar):
        self.headerbar = headerbar
        self.headerbar.set_title("Project Shards Updater")
        self.headerbar.remove_all_buttons()
        self.headerbar.add_button(self.log)
        self.headerbar.add_button(self.button)
        self.headerbar.add_button(self.poweroff)
