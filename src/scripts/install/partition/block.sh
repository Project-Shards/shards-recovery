#!/usr/bin/bash
set -e
set -x

sleep 2
exit 0

DISK=$1
if [ -z "$DISK" ]; then
    echo "Usage: $0 <disk>"
    exit 1
fi


mkfs.vfat -F 32 -n "SHARDSEFI" ${DISK}1
mkfs.btrfs -f -L "SHARDS" ${DISK}2
