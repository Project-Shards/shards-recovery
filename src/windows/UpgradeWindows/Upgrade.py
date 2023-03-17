# Upgrade.py
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
from shard_updater.widgets.UpdateStep import UpdateStep
from shard_updater.utils.threading import RunAsync

@Gtk.Template(resource_path='/al/getcryst/shard/updater/windows/UpgradeWindows/Upgrade.ui')
class Upgrade(Adw.Bin):
    __gtype_name__="Upgrade"

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
    statuspage = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def set_window(self, window):
        self.window = window



    def set_icon(self, icon: str):
        self.statuspage.set_icon_name(icon)

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
        GLib.idle_add(self.set_icon, "shardbottom")
        time.sleep(1)
        root_mount_start(self, finished=False)
        time.sleep(0.5)
        root_mount_start(self, finished=True)
        root_snapshot_start(self, finished=False)
        time.sleep(0.5)
        root_snapshot_start(self, finished=True)
        root_update_start(self, finished=False)
        time.sleep(0.5)
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
        GLib.idle_add(self.set_icon, "shardleft")
        time.sleep(1)
        system_mount_start(self, finished=False)
        time.sleep(0.5)
        system_mount_start(self, finished=True)
        system_snapshot_start(self, finished=False)
        time.sleep(0.5)
        system_snapshot_start(self, finished=True)
        system_update_start(self, finished=False)
        time.sleep(0.5)
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
        GLib.idle_add(self.set_icon, "shardright")
        time.sleep(1)
        desktop_mount_start(self, finished=False)
        time.sleep(0.5)
        desktop_mount_start(self, finished=True)
        desktop_snapshot_start(self, finished=False)
        time.sleep(0.5)
        desktop_snapshot_start(self, finished=True)
        desktop_update_start(self, finished=False)
        time.sleep(0.5)
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
            GLib.idle_add(self.set_icon, "shardfull")
            GLib.idle_add(self.window.upgrade_finished, True)

        GLib.idle_add(self.data.set_expanded, True)
        GLib.idle_add(self.set_icon, "shardtop")
        time.sleep(1)
        data_mount_start(self, finished=False)
        time.sleep(0.5)
        data_mount_start(self, finished=True)
        data_snapshot_start(self, finished=False)
        time.sleep(0.5)
        data_snapshot_start(self, finished=True)
        data_update_start(self, finished=False)
        time.sleep(0.5)
        data_update_start(self, finished=True)
        on_data_finish(self)
