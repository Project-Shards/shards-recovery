# YNDialog.py
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

#@Gtk.Template(resource_path='/al/getcryst/shard/updater/widgets/YNDialog.ui')
class YNDialog():
    __gtype_name__ = 'YNDialog'


    def __init__(
            self,
            header: str,
            body: str,
            yes_text: str,
            no_text: str,
            on_yes,
            on_no,
            window,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.on_yes = on_yes
        self.on_no = on_no
        self.dialog = Adw.MessageDialog(
            heading=header,
            body=body,
        )
        self.dialog.add_response(
            id="no",
            label=no_text,
        )
        self.dialog.add_response(
            id="yes",
            label=yes_text,
        )
        self.dialog.set_transient_for(window)
        self.dialog.set_default_response("yes")
        self.dialog.set_close_response("no")

    def display(self):
        self.dialog.show()
        self.dialog.connect('response', self.on_response)

    def on_response(self, widget, response):
        if response == "yes" and self.on_yes:
            self.on_yes()
        elif response == "no" and self.on_no:
            self.on_no()
        self.dialog.destroy()
