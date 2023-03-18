#!/usr/bin/bash
set -e # Make sure the script quits when a command fails
set -x # Output the commands being ran

mkdir -p /mnt/snapshots # Make sure the snapshot directory exists

echo "Creating Snapshot of Root preloader"
btrfs subvolume snapshot /mnt /mnt/snapshots/ROOT-$(date -I)
