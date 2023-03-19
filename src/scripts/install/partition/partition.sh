#!/usr/bin/bash
set -e
set -x

DISK=$1

if [ -z "$DISK" ]; then
    echo "Usage: $0 <disk>"
    exit 1
fi

if [ ! -b "$DISK" ]; then
    echo "Disk $DISK does not exist"
    exit 1
fi


parted -s $DISK mklabel gpt
parted -S $DISK mkpart fat32 1MiB 512MiB
parted -S $DISK mkpart btrfs 512MiB 100%
