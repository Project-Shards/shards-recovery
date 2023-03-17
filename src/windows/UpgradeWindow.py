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


from gi.repository import Gtk, Adw, GLib, GdkPixbuf, Gdk
import time
from shard_updater.widgets.MenuButton import MenuButton
from shard_updater.utils.threading import RunAsync
from shard_updater.windows.UpgradeWindows.Upgrade import Upgrade
from shard_updater.windows.UpgradeWindows.UpgradeFail import UpgradeFail
from shard_updater.windows.UpgradeWindows.UpgradeFinish import UpgradeFinish

@Gtk.Template(resource_path='/al/getcryst/shard/updater/windows/UpgradeWindow.ui')
class UpgradeWindow(Gtk.Stack):
    __gtype_name__ = 'UpgradeWindow'

    upgrade = Gtk.Template.Child()
    upgradefinish = Gtk.Template.Child()
    upgradefail = Gtk.Template.Child()

    def __init__(self, window, headerbar, **kwargs):
        super().__init__(**kwargs)
        self.window = window
        self.headerbar = headerbar
        self.button = MenuButton(label="Cancel Update", on_clicked=self.on_quit_button_clicked)
        self.upgrade.set_window(self)


    def upgrade_finished(self, success: bool):
        if success:
            self.set_visible_child(self.upgradefinish)
            self.upgradefinish.on_show(self.headerbar)
        else:
            self.set_visible_child(self.upgradefail)
            self.upgradefail.on_show(self.headerbar)

    def on_show(self):
        self.headerbar.set_title("Project Shards Updater")
        self.headerbar.remove_all_buttons()
        self.headerbar.add_button(self.button)
        RunAsync(self.upgrade.root_step)

    def on_quit_button_clicked(self, widget):
        self.window.switch_to_main()
