# LogView.py
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

from gi.repository import Gtk, Adw, GtkSource

@Gtk.Template(resource_path='/al/getcryst/shard/updater/windows/LogView.ui')
class LogView(Adw.Bin):
    __gtype_name__ = 'LogView'

    LogBox = Gtk.Template.Child()

    def __init__(self, logfile: str, **kwargs):
        super().__init__(**kwargs)

        self.logfile = logfile
        scrolled_view = Gtk.ScrolledWindow(vexpand=True, hexpand=True)
        style_scheme_manager = GtkSource.StyleSchemeManager.get_default()
        self.text_buffer = GtkSource.Buffer(
            highlight_syntax=False,
            style_scheme=style_scheme_manager.get_scheme("oblivion"),
        )
        text_view = GtkSource.View(
            buffer=self.text_buffer, show_line_numbers=True, monospace=True
        )
        self.text_buffer = text_view.get_buffer()
        self.buffer_iter = self.text_buffer.get_end_iter()
        self.text_buffer.insert(self.buffer_iter, "Loading log file...")
        scrolled_view.set_child(text_view)
        self.LogBox.append(scrolled_view)

    def on_show(self):
        with open(self.logfile, 'r') as file:
            self.content = file.read()
        self.text_buffer.set_text(self.content, -1)
