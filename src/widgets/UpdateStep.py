# UpdateStep.py
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


@Gtk.Template(resource_path='/al/getcryst/shard/updater/widgets/UpdateStep.ui')
class UpdateStep(Adw.ActionRow):
    __gtype_name__ = "UpdateStep"

    icon_status = Gtk.Template.Child()
    spinner_status = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.spinner_status.set_spinning(False)
        self.set_icon_status(False)

    def set_spinner(self, shown: bool):
        print(shown)
        print("spinner")
        self.spinner_status.set_spinning(shown)
        self.spinner_status.set_visible(shown)
        self.icon_status.set_visible(not shown)

    def set_icon_status(self, finished: bool):
        self.spinner_status.set_visible(False)
        self.icon_status.set_visible(True)
        if finished:
            self.icon_status.set_from_icon_name("test-pass")
            self.icon_status.remove_css_class("update_wait")
            self.icon_status.add_css_class("update_finish")
            self.set_spinner(False)
        else:
            self.icon_status.set_from_icon_name("content-loading-symbolic")
            self.icon_status.remove_css_class("update_finish")
            self.icon_status.add_css_class("update_wait")
            self.set_spinner(False)
