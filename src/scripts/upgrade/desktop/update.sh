#!/usr/bin/bash
set -e # Make sure the script quits when a command fails
set -x # Output the commands being ran

echo "Upgrading Desktop shard at /mnt/"
arch-chroot /mnt/ pacman -Syu --noconfirm

echo "Removing Overlays"
umount /mnt/opt
umount /mnt/var
umount /mnt/usr
