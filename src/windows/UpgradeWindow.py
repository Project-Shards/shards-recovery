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


from gi.repository import Gtk
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
    update_started = False

    def __init__(self, window, headerbar, **kwargs):
        super().__init__(**kwargs)
        self.window = window
        self.headerbar = headerbar
        self.upgrade.set_window(self)


    def upgrade_finished(self, success: bool):
        print("Window height "+ str( self.window.get_allocated_height()))
        print("Window width "+ str( self.window.get_allocated_width()))
        if success:
            self.set_visible_child(self.upgradefinish)
            self.upgradefinish.on_show(
                self.headerbar,
                self,
                self.window.get_allocated_width(),
                self.window.get_allocated_height()
            )
        else:
            self.set_visible_child(self.upgradefail)
            self.upgradefail.on_show(
                self.headerbar,
                self,
                self.window.get_allocated_width(),
                self.window.get_allocated_height()
            )

    def on_show(self):
        self.headerbar.set_title("Project Shards Updater")
        self.headerbar.remove_all_buttons()
        if not self.update_started:
            RunAsync(self.upgrade.root_step)
            self.update_started=True

    def on_quit_button_clicked(self, button):
        self.window.switch_to_main()
