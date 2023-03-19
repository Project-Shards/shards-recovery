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

@Gtk.Template(resource_path='/al/getcryst/shard/updater/windows/InstallWindows/DiskSelect.ui')
class DiskSelect(Gtk.Box):
    __gtype_name__ = 'DiskSelect'

    disk_list = Gtk.Template.Child()
    continue_button = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_disk="/dev/sda"
        testDisk = Disk(diskname="/dev/sda", disksize="10bla (blahajs)", disktype="SSD", group=None, parent=self)
        testDisk2 = Disk(diskname="/dev/sdb", disksize="10bla (blahajs)", disktype="SSD", group=testDisk, parent=self)
        self.disk_list.append(testDisk)
        self.disk_list.append(testDisk2)

    def _set_selected_disk(self, disk: str):
        print(disk)
        self.selected_disk=disk
