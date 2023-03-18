#!/usr/bin/bash
set -e # Make sure the script quits when a command fails
set -x # Output the commands being ran

echo "Upgrading Root shard at /mnt"
arch-chroot /mnt pacman -Syu
