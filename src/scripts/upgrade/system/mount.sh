#!/usr/bin/bash
set -e # Make sure the script quits when a command fails
set -x # Output the commands being ran

echo "Creating bind mount from /mnt/Shards/Data/etc to /mnt/Shards/System/etc"
mount --bind /mnt/Shards/Data/etc /mnt/Shards/System/etc
