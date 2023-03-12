# window.py
#
# Copyright 2023 Unknown
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw, Gtk, Gdk
from shard_updater.windows.RecoveryTerminalWindow import RecoveryTerminalWindow
from shard_updater.windows.InstallWindow import InstallWindow
from shard_updater.widgets.MenuButton import MenuButton
from shard_updater.HeaderBar import HeaderBar

@Gtk.Template(resource_path='/al/getcryst/shard/updater/window.ui')
class ShardUpdaterWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'ShardUpdaterWindow'

    #label = Gtk.Template.Child()
    shard_shell_button = Gtk.Template.Child()
    recovery_button = Gtk.Template.Child()
    browser_button = Gtk.Template.Child()
    reinstall_button = Gtk.Template.Child()
    update_button = Gtk.Template.Child()
    window_box = Gtk.Template.Child()
    main_window = Gtk.Template.Child()
    header_bar = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fullscreen()
#        self.header_bar = HeaderBar(self)
        print(self.header_bar)
        self.header_bar.set_window(self)
        self.header_bar.set_title("Project Shards Recovery")
        self.menu_button = MenuButton("Quit", self.close)
        self.header_bar.add_button(self.menu_button)
        self.current_window = self.main_window
        self.recovery_button.connect("activated", self.show_recovery_terminal)
        self.reinstall_button.connect("activated", self.show_install_window)

        css=b"""
        .window {
            padding-left: 100px;
            padding-right: 100px;
            padding-top: 100px;
            padding-bottom: 100px;
            border-radius: 6px;
            box-shadow: 0 1px 4px 1px alpha(black, 0.13),
              0 1px 10px 5px alpha(black, 0.09),
              0 3px 16px 8px alpha(black, 0.04),
              0 0 0 1px alpha(black, .05);
        }
        .topbutton {
            font-weight: normal;
        }
        .disk {
            padding-left: 50px;
            padding-right: 50px;
            padding-top: 30px;
            padding-bottom: 30px;
            border-radius: 6px;
            box-shadow: 0 1px 3px 1px alpha(black, 0.13),
              0 1px 1px 1px alpha(black, 0.09),
              0 1px 1px 1px alpha(black, 0.04),
              0 0 0 1px alpha(black, .05);
        }
        .rounded {
            border-radius: 10px;
        }
        """
        provider = Gtk.CssProvider()
        provider.load_from_data(data=css)
        Gtk.StyleContext.add_provider_for_display(
            display=Gdk.Display.get_default(),
            provider=provider,
            priority=Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

    def show_install_window(self, widget):
        print("show install window")
        self.current_window.set_visible(False)
        self.install_window=InstallWindow(self, self.header_bar)
        self.window_box.append(self.install_window)
        self.current_window = self.install_window

    def show_recovery_terminal(self, widget):
        print("show recovery terminal")
        self.current_window.set_visible(False)
        self.recovery_terminal=RecoveryTerminalWindow(self, self.header_bar)
        self.window_box.append(self.recovery_terminal)
        self.current_window = self.recovery_terminal

    def close(self, widget):
        print("close")
        self.destroy()

    def switch_to_main(self):
        self.main_window.set_visible(True)
        self.current_window.set_visible(False)
        self.current_window = self.main_window
        self.header_bar.set_title("Project Shards Recovery")
        self.header_bar.remove_all_buttons()
        self.header_bar.add_button(self.menu_button)
