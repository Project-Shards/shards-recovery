# Disk.py
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

@Gtk.Template(resource_path='/al/getcryst/shard/updater/widgets/Disk.ui')
class Disk(Gtk.ToggleButton):
    __gtype_name__ = "Disk"

    DiskType = Gtk.Template.Child()
    DiskName = Gtk.Template.Child()
    DiskSize = Gtk.Template.Child()

    def __init__(self, diskname, disksize, disktype, group, parent, **kwargs):
        super().__init__(**kwargs)
        self.parent = parent
        self.name=diskname
        self.size=disksize
        self.type=disktype
        self.DiskName.set_label(diskname)
        self.DiskSize.set_label(disksize)
        if "SSD" in self.type:
            self.DiskType.set_from_icon_name("drive-harddisk-solidstate-symbolic")
        else:
            self.DiskType.set_from_icon_name("drive-harddisk-symbolic")
        self.connect("toggled", self._on_selected)
        if group is not None:
            self.set_group(group)

    def _on_selected(self, button):
        self.parent._set_selected_disk(self.name)
