#!/usr/bin/bash
set -e # Make sure the script quits when a command fails
set -x # Output the commands being ran

echo "Upgrading Data shard at /mnt/"
arch-chroot /mnt/ pacman -Syu --noconfirm

echo "Removing Overlays"
umount /mnt/opt
umount /mnt/var
umount /mnt/usr

echo "Remvong bind mounts"
umount /mnt/etc
umount /mnt/boot

echo "Unmount Shards"
umount /mnt/Shards/System
umount /mnt/Shards/Desktop
umount /mnt/Shards/Data

echo "Unmounting Root shard"
umount /mnt
