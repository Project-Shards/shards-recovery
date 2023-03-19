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

from gi.repository import Gtk, Adw, GLib
from shard_updater.utils.threading import RunAsync
import subprocess
import sys
import time

@Gtk.Template(resource_path='/al/getcryst/shard/updater/windows/InstallWindows/InstallProgress.ui')
class InstallProgress(Gtk.Box):
    __gtype_name__ = 'InstallProgress'

    reboot_button = Gtk.Template.Child()
    progress_bar = Gtk.Template.Child()
    stop_install = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.scriptdir=sys.path[1]+"/shard_updater/scripts/install/"

    def set_window(self, window):
        self.window = window

    def check_command(self, output: subprocess.CompletedProcess):
        with open('/tmp/shardsrecovery.log', 'a') as log:
            log.write(output.stdout.decode("utf-8"))
        if output.returncode != 0:
            self.progressbar_cubic_ease(1)
            self.progress_bar.set_text(self.progress_bar.get_text()+" Failed")
            self.window.on_install_finished(False)
            self.stop_install=True

    def progressbar_cubic_ease(self, fraction):
        limit = (0, 1)
        start=0
        end=100
        duration=100
        def func(t: float) -> float:
            return (t - 1) * (t - 1) * (t - 1) + 1

        def ease(alpha: float) -> float:
            t = limit[0] * (1 - alpha) + limit[1] * alpha
            t /= duration
            a = func(t)
            return end * a + start * (1 - a)

        for i in range(int(self.progress_bar.get_fraction()*100), int(fraction*100)):
            time.sleep(0.01)
            print("i "+str(i))
            print(ease(i)/100)
            GLib.idle_add(self.progress_bar.set_fraction, (i+ease(i)/100)/100)

    def on_show(self, selected_disk):
        self.selected_disk = selected_disk
        RunAsync(self.install)

    def install(self):
        if self.stop_install:
            return
        self.progress_bar.set_text("Partitioning disk")
        self.progress_bar.set_fraction(0)
        out = subprocess.run(
            [self.scriptdir+"/partition/partition.sh", self.selected_disk],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        self.check_command(out)
        if self.stop_install:
            return
        out = subprocess.run(
            ["pkexec", self.scriptdir+"partition/"+("nvme" if "nvme" in self.selected_disk else "block")+".sh", self.selected_disk],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        self.check_command(out)
        if self.stop_install:
            return
        out = subprocess.run(
            ["pkexec", self.scriptdir+"/partition/shards.sh"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        self.check_command(out)
        if self.stop_install:
            return
        self.progressbar_cubic_ease(0.14)
        self.progress_bar.set_text("Installing Recovery")
        out = subprocess.run(
            ["pkexec", self.scriptdir+"/recovery.sh"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        self.check_command(out)
        if self.stop_install:
            return
        self.progressbar_cubic_ease(0.28)
        self.progress_bar.set_text("Installing Root preloader")
        out = subprocess.run(
            ["pkexec", self.scriptdir+"/root.sh"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        self.check_command(out)
        if self.stop_install:
            return
        self.progressbar_cubic_ease(0.42)
        self.progress_bar.set_text("Installing Data Shard")
        out = subprocess.run(
            ["pkexec", self.scriptdir+"/data.sh"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        self.check_command(out)
        if self.stop_install:
            return
        self.progressbar_cubic_ease(0.56)
        self.progress_bar.set_text("Installing System Shard")
        out = subprocess.run(
            ["pkexec", self.scriptdir+"/system.sh"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        self.check_command(out)
        if self.stop_install:
            return
        self.progressbar_cubic_ease(0.7)
        self.progress_bar.set_text("Installing Desktop Shard")
        out = subprocess.run(
            ["pkexec", self.scriptdir+"/desktop.sh"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        self.check_command(out)
        if self.stop_install:
            return
        self.progressbar_cubic_ease(0.84)
        self.progress_bar.set_text("Installing Bootloader")
        out = subprocess.run(
            ["pkexec", self.scriptdir+"/bootloader.sh"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        self.check_command(out)
        if self.stop_install:
            return
        self.progressbar_cubic_ease(1)
        self.progress_bar.set_text("Install Finished")
        self.window.on_install_finished(True)
