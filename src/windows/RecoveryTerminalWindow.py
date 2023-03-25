# RecoveryTerminalWindow.py
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
from gi.repository import Gtk, Adw, Vte, Pango, GLib
from shard_updater.widgets.MenuButton import MenuButton
from shard_updater.HeaderBar import HeaderBar

@Gtk.Template(resource_path='/al/getcryst/shard/updater/windows/RecoveryTerminalWindow.ui')
class RecoveryTerminalWindow(Adw.Bin):
    __gtype_name__ = 'RecoveryTerminalWindow'

#    terminal_box = Gtk.Template.Child()
    
    def __init__(
            self,
            window,
            headerbar: HeaderBar,
            command: list=["bash"],
            **kwargs
    ):
        super().__init__(**kwargs)
        self.window = window
        self.headerbar = headerbar

        self.button = MenuButton(
            label="Quit Terminal",
            on_clicked=self.on_quit_button_clicked
        )
        self.command = command
        self.vte_instance = Vte.Terminal()
        self.vte_instance.set_cursor_blink_mode(Vte.CursorBlinkMode.ON)
        self.vte_instance.set_font(Pango.FontDescription("Source Code Pro Regular 12"))
        self.set_child(self.vte_instance)
        self.vte_instance.connect("child-exited", self.on_quit_button_clicked)

    def on_show(self):
        self.headerbar.set_title("Recovery Terminal")
        self.headerbar.remove_all_buttons()
        self.headerbar.add_button(self.button)

        self.vte_instance.spawn_async(
            Vte.PtyFlags.DEFAULT,
            ".", #cwd
            self.command,
            [], #envvars
            GLib.SpawnFlags.DO_NOT_REAP_CHILD,
            None,
            None,
            -1,
            None,
            None,
        )
        
    def on_quit_button_clicked(self, button):
        self.window.switch_to_main()
