#!/usr/bin/bash
set -e # Make sure the script quits when a command fails
set -x # Output the commands being ran

echo "Creating Overlay with System and Desktop for /mnt/usr"
mount -t overlay overlay -o lowerdir=/Shards/System/usr,upperdir=/Shards/Desktop/usr,workdir=/Shards/Desktop/tmp/usr /mnt/usr

echo "Creating Overlay with System and Desktop for /mnt/var"
mount -t overlay overlay -o lowerdir=/Shards/System/var,upperdir=/Shards/Desktop/var,workdir=/Shards/Desktop/tmp/var /mnt/var

echo "Creating Overlay with System and Desktop for /mnt/opt"
mount -t overlay overlay -o lowerdir=/Shards/System/opt,upperdir=/Shards/Desktop/opt,workdir=/Shards/Desktop/tmp/opt /mnt/opt

echo "Creating bind mount from /mnt/Shards/Data/etc to /mnt/etc"
mount --bind /mnt/Shards/Data/etc /mnt/etc

echo "Creatin bind mount from /mnt/Shards/System/boot to /mnt/boot"
mount --bind /mnt/Shards/System/boot /mnt/boot
