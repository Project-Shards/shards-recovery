#!/usr/bin/bash
set -e # Make sure the script quits when a command fails
set -x # Output the commands being ran

mkdir -p /mnt/Shards/System/snapshots # Make sure the snapshot directory exists

echo "Creating Snapshot of System Shard"
btrfs subvolume snapshot /mnt/Shards/System /mnt/Shards/System/snapshots/SYSTEM-$(date -I)
