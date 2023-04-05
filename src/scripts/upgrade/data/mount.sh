#!/usr/bin/bash
set -e # Make sure the script quits when a command fails
set -x # Output the commands being ran

ROOTDISK=$(df / | awk '{print $1}' | grep -v "Filesystem") # Get the root disk

echo "Remount /mnt/Shards/Desktop as read-only"
sync
umount /mnt/Shards/Desktop
mount -o ro,subvol=Desktop "$ROOTDISK" /mnt/Shards/Desktop

echo "Creating Overlay with System, Desktop and Data for /mnt/usr"
mount -t overlay overlay -o lowerdir=/mnt/Shards/System/usr:/mnt/Shards/Desktop/usr,upperdir=/mnt/Shards/Data/usr,workdir=/mnt/Shards/Data/tmp/usr /mnt/usr

echo "Creating Overlay with System, Desktop and Data for /mnt/var"
mount -t overlay overlay -o lowerdir=/mnt/Shards/System/var:/mnt/Shards/Desktop/var,upperdir=/mnt/Shards/Data/var,workdir=/mnt/Shards/Data/tmp/var /mnt/var

echo "Creating Overlay with System, Desktop and Data for /mnt/opt"
mount -t overlay overlay -o lowerdir=/mnt/Shards/System/opt:/mnt/Shards/Desktop/opt,upperdir=/mnt/Shards/Data/opt,workdir=/mnt/Shards/Data/tmp/opt /mnt/opt
