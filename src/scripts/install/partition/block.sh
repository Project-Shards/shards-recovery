#!/usr/bin/bash
set -e
set -x

DISK=$1
if [ -z "$DISK" ]; then
    echo "Usage: $0 <disk>"
    exit 1
fi

sleep 1
exit 0

mkfs.vfat -F 32 -n "BOOT" ${DISK}1
mkfs.btrfs -f -L "SHARDS" ${DISK}2
