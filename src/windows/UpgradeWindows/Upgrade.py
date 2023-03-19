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
import subprocess
import sys
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
    upgrade_failed = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.scriptdir = sys.path[1]+"/shard_updater/scripts/upgrade/"

    def set_window(self, window):
        self.window = window

    def set_icon(self, icon: str):
        self.statuspage.set_icon_name(icon)

    def check_fail(self):
        if self.upgrade_failed:
            self.window.upgrade_finished(False)

    def write_to_log(self, output: str):
        with open('/tmp/shardsrecovery.log', 'a') as log:
            log.write(output)

    def root_step(self):

        def root_mount_start(self):
            if self.upgrade_failed:
                return
            GLib.idle_add(self.mount_root.set_spinner, True)
            out = subprocess.run(
                ["pkexec", self.scriptdir+"root/mount.sh"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT
            )
            self.write_to_log(out.stdout.decode("utf-8"))
            if out.returncode == 0:
                GLib.idle_add(self.mount_root.set_icon_status, True)
            else:
                self.upgrade_failed=True

        def root_snapshot_start(self):
            if self.upgrade_failed:
                return
            GLib.idle_add(self.snapshot_root.set_spinner, True)
            out = subprocess.run(
                ["pkexec", self.scriptdir+"root/snapshot.sh"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT
            )
            self.write_to_log(out.stdout.decode("utf-8"))
            if out.returncode == 0:
                GLib.idle_add(self.snapshot_root.set_icon_status, True)
            else:
                self.upgrade_failed=True

        def root_update_start(self):
            if self.upgrade_failed:
                return
            GLib.idle_add(self.update_root.set_spinner, True)
            out = subprocess.run(
                ["pkexec", self.scriptdir+"root/update.sh"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT
            )
            self.write_to_log(out.stdout.decode("utf-8"))
            if out.returncode == 0:
                GLib.idle_add(self.update_root.set_icon_status, True)
            else:
                self.upgrade_failed=True


        def on_root_finish(self):
            if self.upgrade_failed:
                return
            GLib.idle_add(self.root.set_icon_name, "test-pass")
            GLib.idle_add(self.root.set_expanded, False)
            self.system_step()

        GLib.idle_add(self.root.set_expanded, True)
        GLib.idle_add(self.set_icon, "shardbottom")
        root_mount_start(self)
        GLib.idle_add(self.check_fail)
        root_snapshot_start(self)
        GLib.idle_add(self.check_fail)
        root_update_start(self)
        GLib.idle_add(self.check_fail)
        on_root_finish(self)


    def system_step(self):

        def system_mount_start(self):
            if self.upgrade_failed:
                return
            GLib.idle_add(self.mount_system.set_spinner, True)
            out = subprocess.run(
                ["pkexec", self.scriptdir+"system/mount.sh"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT
            )
            self.write_to_log(out.stdout.decode("utf-8"))
            if out.returncode == 0:
                GLib.idle_add(self.mount_system.set_icon_status, True)
            else:
                self.upgrade_failed=True

        def system_snapshot_start(self):
            if self.upgrade_failed:
                return
            GLib.idle_add(self.snapshot_system.set_spinner, True)
            out = subprocess.run(
                ["pkexec", self.scriptdir+"system/snapshot.sh"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT
            )
            self.write_to_log(out.stdout.decode("utf-8"))
            if out.returncode == 0:
                GLib.idle_add(self.snapshot_system.set_icon_status, True)
            else:
                self.upgrade_failed=True

        def system_update_start(self):
            if self.upgrade_failed:
                return
            GLib.idle_add(self.update_system.set_spinner, True)
            out = subprocess.run(
                ["pkexec", self.scriptdir+"system/update.sh"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT
            )
            self.write_to_log(out.stdout.decode("utf-8"))
            if out.returncode == 0:
                GLib.idle_add(self.update_system.set_icon_status, True)
            else:
                self.upgrade_failed=True

        def on_system_finish(self):
            if self.upgrade_failed:
                return
            GLib.idle_add(self.system.set_icon_name, "test-pass")
            GLib.idle_add(self.system.set_expanded, False)
            self.desktop_step()

        GLib.idle_add(self.system.set_expanded, True)
        GLib.idle_add(self.set_icon, "shardleft")
        system_mount_start(self)
        GLib.idle_add(self.check_fail)
        system_snapshot_start(self)
        GLib.idle_add(self.check_fail)
        system_update_start(self)
        GLib.idle_add(self.check_fail)
        on_system_finish(self)

    def desktop_step(self):

        def desktop_mount_start(self):
            if self.upgrade_failed:
                return
            GLib.idle_add(self.mount_desktop.set_spinner, True)
            out = subprocess.run(
                ["pkexec", self.scriptdir+"desktop/mount.sh"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT
            )
            self.write_to_log(out.stdout.decode("utf-8"))
            if out.returncode == 0:
                GLib.idle_add(self.mount_desktop.set_icon_status, True)
            else:
                self.upgrade_failed=True

        def desktop_snapshot_start(self):
            if self.upgrade_failed:
                return
            GLib.idle_add(self.snapshot_desktop.set_spinner, True)
            out = subprocess.run(
                ["pkexec", self.scriptdir+"desktop/snapshot.sh"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT
            )
            if out.returncode == 0:
                GLib.idle_add(self.snapshot_desktop.set_icon_status, True)
            else:
                self.upgrade_failed=True

        def desktop_update_start(self):
            if self.upgrade_failed:
                return
            GLib.idle_add(self.update_desktop.set_spinner, True)
            out = subprocess.run(
                ["pkexec", self.scriptdir+"desktop/update.sh"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT
            )
            self.write_to_log(out.stdout.decode("utf-8"))
            if out.returncode == 0:
                GLib.idle_add(self.update_desktop.set_icon_status, True)
            else:
                self.upgrade_failed=True

        def on_desktop_finish(self):
            if self.upgrade_failed:
                return
            GLib.idle_add(self.desktop.set_icon_name, "test-pass")
            GLib.idle_add(self.desktop.set_expanded, False)
            self.data_step()

        GLib.idle_add(self.desktop.set_expanded, True)
        GLib.idle_add(self.set_icon, "shardright")
        desktop_mount_start(self)
        GLib.idle_add(self.check_fail)
        desktop_snapshot_start(self)
        GLib.idle_add(self.check_fail)
        desktop_update_start(self)
        GLib.idle_add(self.check_fail)
        on_desktop_finish(self)


    def data_step(self):

        def data_mount_start(self):
            if self.upgrade_failed:
                return
            GLib.idle_add(self.mount_data.set_spinner, True)
            out = subprocess.run(
                ["pkexec", self.scriptdir+"data/mount.sh"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT
            )
            self.write_to_log(out.stdout.decode("utf-8"))
            if out.returncode == 0:
                GLib.idle_add(self.mount_data.set_icon_status, True)
            else:
                self.upgrade_failed=True

        def data_snapshot_start(self):
            if self.upgrade_failed:
                return
            GLib.idle_add(self.snapshot_data.set_spinner, True)
            out = subprocess.run(
                ["pkexec", self.scriptdir+"data/snapshot.sh"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT
            )
            self.write_to_log(out.stdout.decode("utf-8"))
            if out.returncode == 0:
                GLib.idle_add(self.snapshot_data.set_icon_status, True)
            else:
                self.upgrade_failed=True


        def data_update_start(self):
            if self.upgrade_failed:
                return
            GLib.idle_add(self.update_data.set_spinner, True)
            out = subprocess.run(
                ["pkexec", self.scriptdir+"data/update.sh"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT
            )
            self.write_to_log(out.stdout.decode("utf-8"))
            if out.returncode == 0:
                GLib.idle_add(self.update_data.set_icon_status, True)
            else:
                self.upgrade_failed=True

        def on_data_finish(self):
            if self.upgrade_failed:
                return
            GLib.idle_add(self.data.set_icon_name, "test-pass")
            GLib.idle_add(self.data.set_expanded, False)
            GLib.idle_add(self.set_icon, "shardfull")
            GLib.idle_add(self.window.upgrade_finished, True)

        GLib.idle_add(self.data.set_expanded, True)
        GLib.idle_add(self.set_icon, "shardtop")
        time.sleep(1)
        data_mount_start(self)
        GLib.idle_add(self.check_fail)
        data_snapshot_start(self)
        GLib.idle_add(self.check_fail)
        data_update_start(self)
        GLib.idle_add(self.check_fail)
        on_data_finish(self)
