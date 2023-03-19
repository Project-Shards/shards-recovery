#!/usr/bin/bash
set -e
set -x

DISK=$1

mkfs.vfat -F32 -n "EFI" ${DISK}p1
mkfs.btrfs -f -L "SHARDS" ${DISK}p2
