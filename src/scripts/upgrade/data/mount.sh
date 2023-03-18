#!/usr/bin/bash
set -e # Make sure the script quits when a command fails
set -x # Output the commands being ran

echo "Remount /mnt/Shards/Desktop as read-only"
mount -o ro,remount /mnt/Shards/Desktop

echo "Creating Overlay with System, Desktop and Data for /mnt/usr"
mount -t overlay overlay -o lowerdir=/Shards/System/usr:/Shards/Desktop/usr,upperdir=/Shards/Data/usr,workdir=/Shards/Data/tmp/usr /usr

echo "Creating Overlay with System, Desktop and Data for /mnt/var"
mount -t overlay overlay -o lowerdir=/Shards/System/var:/Shards/Desktop/var,upperdir=/Shards/Data/var,workdir=/Shards/Data/tmp/var /var

echo "Creating Overlay with System, Desktop and Data for /mnt/opt"
mount -t overlay overlay -o lowerdir=/Shards/System/opt:/Shards/Desktop/opt,upperdir=/Shards/Data/opt,workdir=/Shards/Data/tmp/opt /opt
