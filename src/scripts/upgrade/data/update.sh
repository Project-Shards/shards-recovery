#!/usr/bin/bash
set -e # Make sure the script quits when a command fails
set -x # Output the commands being ran

echo "Upgrading Data shard at /mnt/"
arch-chroot /mnt/ pacman -Syu

echo "Removing Overlays"
umount /mnt/opt
umount /mnt/var
umount /mnt/usr

echo "Remvong bind mounts"
umuont /mnt/etc
umount /mnt/boot

echo "Unmounting Root shard"
umount /mnt
