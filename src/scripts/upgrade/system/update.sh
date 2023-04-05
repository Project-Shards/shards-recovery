#!/usr/bin/bash
set -e # Make sure the script quits when a command fails
set -x # Output the commands being ran

echo "Upgrading System shard at /mnt/Shards/System"
arch-chroot /mnt/Shards/System pacman -Syu --noconfirmx

echo "Unmounting /mnt/Shards/System/etc"
umount /mnt/Shards/System/etc
