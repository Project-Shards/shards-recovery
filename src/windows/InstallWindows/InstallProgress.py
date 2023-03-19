# InstallProgress.py
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
import sys
sys.path.append("/home/axtlos/.local/share/shard_installer/shard_installer")
from shard_installer.functions.partition import Partition
from shard_installer.functions.shards import Shards
from shard_installer.functions.bootloader import Bootloader

@Gtk.Template(resource_path='/al/getcryst/shard/updater/windows/InstallWindows/InstallProgress.ui')
class InstallProgress(Gtk.Box):
    __gtype_name__ = 'InstallProgress'

    reboot_button = Gtk.Template.Child()
    progress_bar = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_show(self, selected_disk):
        self.selected_disk = selected_disk
        self.progress_bar.set_fraction(0)
        partition=Partition(selected_disk)
        partition.start_partition()
        self.progress_bar.set_fraction(0.16)
        Shards.setupRecovery(mountpoint="/mnt", disk=partition, crash=False)
        self.progress_bar.set_fraction(0.32)
        Shards.setupRoot(mountpoint="/mnt", disk=partition, crash=False)
        self.progress_bar.set_fraction(0.48)
        Shards.setupData(mountpoint="/mnt/Shards/Data", crash=False)
        self.progress_bar.set_fraction(0.64)
        Shards.setupSystem(mountpoint="/mnt/Shards/System", crash=False)
        self.progress_bar.set_fraction(0.8)
        Shards.setupDesktop(mountpoint="/mnt", disk=partition, crash=False)
        self.progress_bar.set_fraction(0.1)
