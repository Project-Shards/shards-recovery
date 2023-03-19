# DiskSelect.py
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
from shard_updater.widgets.Disk import Disk
import subprocess

@Gtk.Template(resource_path='/al/getcryst/shard/updater/windows/InstallWindows/DiskSelect.ui')
class DiskSelect(Gtk.Box):
    __gtype_name__ = 'DiskSelect'

    disk_list = Gtk.Template.Child()
    continue_button = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.disks = []
        self.get_disks()
        self.selected_disk=None
        firstdisk = Disk(diskname=self.disks[0], disksize=self.get_disk_size(self.disks[0]), disktype=self.get_disk_type(self.disks[0]), group=None, parent=self)
        firstdisk.add_css_class("first-disk")
        self.disk_list.append(firstdisk)
        for i in self.disks:
            if i == self.disks[0]:
                continue
            disk = Disk(diskname=i, disksize=self.get_disk_size(i), disktype=self.get_disk_type(i), group=firstdisk, parent=self)
            firstdisk.remove_css_class("first-disk")
            self.disk_list.append(disk)

    def get_disks(self):
        output = subprocess.run(["lsblk", "-pdo", "NAME"], capture_output=True, text=True).stdout
        output = output.split()
        output = [x for x in output if "zram" not in x]
        output = [x for x in output if "NAME" not in x]
        output = [x for x in output if "loop" not in x]
        output = [x for x in output if "sr" not in x]
        output = [x for x in output if "fd" not in x]
        self.disks=output

    def get_disk_type(self, disk):
        output = subprocess.run(["lsblk", "-d", "-o", "rota", disk], capture_output=True, text=True).stdout
        output = output.split()
        output = [x for x in output if "ROTA" not in x]

        if len(output) > 0:
            if output[0] == "0":
                return "Solid-State Drive (SSD)"
            elif output[0] == "1":
                return "Hard Disk (HDD)"  # maybe Rotational Drive?

        print(f"No disk found with name: {disk}, assuming unknown.")
        return "Drive type unknown"


    def get_disk_size(self, disk: str) -> str:
        output = subprocess.run(["lsblk", "-pdbo", "SIZE", disk], capture_output=True, text=True).stdout
        output = output.split()
        output = [x for x in output if "SIZE" not in x]

        if len(output) == 0:
            print(f"No disk found with name: {disk}, assuming zero.")
            size = 0
        else:
            size = int(output[0])

        print(disk + ":" + str(size))
        if size < 1000**3:
            size = size / 1000**2
            return f"{size: .2f} MB"
        elif size < 1000**4:
            size = size / 1000**3
            return f"{size: .2f} GB"
        else:
            size = size / 1000**4
            return f"{size: .2f} TB"


    def _set_selected_disk(self, disk: str):
        print(disk)
        self.selected_disk=disk
