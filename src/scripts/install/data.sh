#!/usr/bin/bash
set -e
set -x


echo "-- Creating Data directories --"
mkdir -p /mnt/Shards/Data/{etc,opt,usr,var,tmp}
mkdir -p /mnt/Shards/Data/tmp/{opt,usr,var}
