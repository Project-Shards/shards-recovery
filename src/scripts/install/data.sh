#!/usr/bin/bash
set -e
set -x

sleep 1
exit 0

echo "-- Creating Data directories --"
mkdir -p /mnt/Shards/Data/{etc,opt,usr,var,tmp}
mkdir -p /mnt/Shards/Data/tmp/{opt,usr,var}
