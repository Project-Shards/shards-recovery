#!/usr/bin/bash
set -e # Make sure the script quits when a command fails
set -x # Output the commands being ran

ROOTDISK = $(df / | awk '{print $1}' | grep -v "Filesystem") # Get the root disk

echo "Mounting Root shard at /mnt"
mount $ROOTDISK /mnt -o subvol=Root

echo "Mounting System shard at /mnt/Shards/System"
mount $ROOT /mnt/Shards/System -o subvol=System

echo "Mounting Desktop shard at /mnt/Shards/Desktop"
mount $ROOT /mnt/Shards/Desktop -o subvol=Desktop

echo "Mounting Data shard at /mnt/Shards/Data"
mount $ROOT /mnt/Shards/Data -o subvol=Data
