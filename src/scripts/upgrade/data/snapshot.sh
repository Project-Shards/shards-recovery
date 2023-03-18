#!/usr/bin/bash
set -e # Make sure the script quits when a command fails
set -x # Output the commands being ran

mkdir -p /mnt/Shards/Data/snapshots # Make sure the snapshot directory exists

echo "Creating Snapshot of Desktop Shard"
btrfs subvolume snapshot /mnt/Shards/Data /mnt/Shards/Data/snapshots/DATA-$(date -I)
