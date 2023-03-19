#!/usr/bin/bash
set -e
set -x


mount /dev/disk/by-label/SHARDS /mnt
btrfs subvolume create /mnt/Root
btrfs subvolume create /mnt/System
btrfs subvolume create /mnt/Data
btrfs subvolume create /mnt/Recovery
btrfs subvolume create /mnt/Desktop
btrfs subvolume create /mnt/Users
umount /mnt
