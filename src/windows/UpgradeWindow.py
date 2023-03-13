# UpgraedWindow.py
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
from shard_updater.widgets.UpdateStep import UpdateStep
from shard_updater.utils.threading import RunAsync

@Gtk.Template(resource_path='/al/getcryst/shard/updater/windows/UpgradeWindow.ui')
class UpgradeWindow(Adw.Bin):
    __gtype_name__ = 'UpgradeWindow'

    root = Gtk.Template.Child()
    mount_root = Gtk.Template.Child()
    snapshot_root = Gtk.Template.Child()
    update_root = Gtk.Template.Child()
    system = Gtk.Template.Child()
    mount_system = Gtk.Template.Child()
    snapshot_system = Gtk.Template.Child()
    update_system = Gtk.Template.Child()
    desktop = Gtk.Template.Child()
    mount_desktop = Gtk.Template.Child()
    snapshot_desktop = Gtk.Template.Child()
    update_desktop = Gtk.Template.Child()
    data = Gtk.Template.Child()
    mount_data = Gtk.Template.Child()
    snapshot_data = Gtk.Template.Child()
    update_data = Gtk.Template.Child()


    def __init__(self, window, headerbar, **kwargs):
        super().__init__(**kwargs)
        self.window = window
        self.headerbar = headerbar
        self.button = MenuButton(label="Cancel Update", on_clicked=self.on_quit_button_clicked)


    def on_show(self):
        self.headerbar.set_title("Project Shards Updater")
        self.headerbar.remove_all_buttons()
        self.headerbar.add_button(self.button)
        RunAsync(self.root_step)

    def on_quit_button_clicked(self, widget):
        self.window.switch_to_main()

    def root_step(self):

        def root_mount_start(self, finished: bool):
            GLib.idle_add(self.mount_root.set_spinner, not finished)
            if finished:
                GLib.idle_add(self.mount_root.set_icon_status, finished)

        def root_snapshot_start(self, finished: bool):
            GLib.idle_add(self.snapshot_root.set_spinner, not finished)
            if finished:
                GLib.idle_add(self.snapshot_root.set_icon_status, finished)

        def root_update_start(self, finished: bool):
            GLib.idle_add(self.update_root.set_spinner, not finished)
            if finished:
                GLib.idle_add(self.update_root.set_icon_status, finished)

        def on_root_finish(self):
            GLib.idle_add(self.root.set_icon_name, "test-pass")
            GLib.idle_add(self.root.set_expanded, False)
            self.system_step()

        GLib.idle_add(self.root.set_expanded, True)
        time.sleep(3)
        root_mount_start(self, finished=False)
        time.sleep(3)
        root_mount_start(self, finished=True)
        root_snapshot_start(self, finished=False)
        time.sleep(3)
        root_snapshot_start(self, finished=True)
        root_update_start(self, finished=False)
        time.sleep(3)
        root_update_start(self, finished=True)
        on_root_finish(self)


    def system_step(self):

        def system_mount_start(self, finished: bool):
            GLib.idle_add(self.mount_system.set_spinner, not finished)
            if finished:
                GLib.idle_add(self.mount_system.set_icon_status, finished)

        def system_snapshot_start(self, finished: bool):
            GLib.idle_add(self.snapshot_system.set_spinner, not finished)
            if finished:
                GLib.idle_add(self.snapshot_system.set_icon_status, finished)

        def system_update_start(self, finished: bool):
            GLib.idle_add(self.update_system.set_spinner, not finished)
            if finished:
                GLib.idle_add(self.update_system.set_icon_status, finished)

        def on_system_finish(self):
            GLib.idle_add(self.system.set_icon_name, "test-pass")
            GLib.idle_add(self.system.set_expanded, False)
            self.desktop_step()

        GLib.idle_add(self.system.set_expanded, True)
        time.sleep(3)
        system_mount_start(self, finished=False)
        time.sleep(3)
        system_mount_start(self, finished=True)
        system_snapshot_start(self, finished=False)
        time.sleep(3)
        system_snapshot_start(self, finished=True)
        system_update_start(self, finished=False)
        time.sleep(3)
        system_update_start(self, finished=True)
        on_system_finish(self)

    def desktop_step(self):

        def desktop_mount_start(self, finished: bool):
            GLib.idle_add(self.mount_desktop.set_spinner, not finished)
            if finished:
                GLib.idle_add(self.mount_desktop.set_icon_status, finished)

        def desktop_snapshot_start(self, finished: bool):
            GLib.idle_add(self.snapshot_desktop.set_spinner, not finished)
            if finished:
                GLib.idle_add(self.snapshot_desktop.set_icon_status, finished)

        def desktop_update_start(self, finished: bool):
            GLib.idle_add(self.update_desktop.set_spinner, not finished)
            if finished:
                GLib.idle_add(self.update_desktop.set_icon_status, finished)

        def on_desktop_finish(self):
            GLib.idle_add(self.desktop.set_icon_name, "test-pass")
            GLib.idle_add(self.desktop.set_expanded, False)
            self.data_step()

        GLib.idle_add(self.desktop.set_expanded, True)
        time.sleep(3)
        desktop_mount_start(self, finished=False)
        time.sleep(3)
        desktop_mount_start(self, finished=True)
        desktop_snapshot_start(self, finished=False)
        time.sleep(3)
        desktop_snapshot_start(self, finished=True)
        desktop_update_start(self, finished=False)
        time.sleep(3)
        desktop_update_start(self, finished=True)
        on_desktop_finish(self)


    def data_step(self):

        def data_mount_start(self, finished: bool):
            GLib.idle_add(self.mount_data.set_spinner, not finished)
            if finished:
                GLib.idle_add(self.mount_data.set_icon_status, finished)

        def data_snapshot_start(self, finished: bool):
            GLib.idle_add(self.snapshot_data.set_spinner, not finished)
            if finished:
                GLib.idle_add(self.snapshot_data.set_icon_status, finished)

        def data_update_start(self, finished: bool):
            GLib.idle_add(self.update_data.set_spinner, not finished)
            if finished:
                GLib.idle_add(self.update_data.set_icon_status, finished)

        def on_data_finish(self):
            GLib.idle_add(self.data.set_icon_name, "test-pass")
            GLib.idle_add(self.data.set_expanded, False)

        GLib.idle_add(self.data.set_expanded, True)
        time.sleep(3)
        data_mount_start(self, finished=False)
        time.sleep(3)
        data_mount_start(self, finished=True)
        data_snapshot_start(self, finished=False)
        time.sleep(3)
        data_snapshot_start(self, finished=True)
        data_update_start(self, finished=False)
        time.sleep(3)
        data_update_start(self, finished=True)
        on_data_finish(self)
