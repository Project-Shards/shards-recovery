#!/usr/bin/bash
set -e
set -x

sleep 2
exit 0

echo "-- Creating Overlay mounts for System and Desktop --"
mkdir -p /mnt/Shards/Desktop/{usr,var,opt,tmp}
mkdir -p /mnt/Shards/Desktop/tmp/{usr,var,opt}
mount -t overlay overlay -o lowerdir=/mnt/Shards/System/usr,upperdir=/mnt/Shards/Desktop/usr,workdir=/mnt/Shards/Desktop/tmp/usr /mnt/usr
mount -t overlay overlay -o lowerdir=/mnt/Shards/System/var,upperdir=/mnt/Shards/Desktop/var,workdir=/mnt/Shards/Desktop/tmp/var /mnt/var
mount -t overlay overlay -o lowerdir=/mnt/Shards/System/opt,upperdir=/mnt/Shards/Desktop/opt,workdir=/mnt/Shards/Desktop/tmp/opt /mnt/opt

echo "-- Creating bind mount from /Shards/Data/etc to /etc"
mount --bind /mnt/Shards/Data/etc /mnt/etc

echo "-- Creating bind mount from /Shards/System/boot to /boot"
mount --bind /mnt/Shards/System/boot /mnt/boot

echo "-- Creating bind mount from /Shards/Users to /home --"
mount --bind /mnt/Shards/Users /mnt/home

echo "-- Mounting EFI partition --"
mount /dev/disk/by-label/EFI /mnt/boot/efi

echo "-- Installing Desktop Shard --"
pacstrap -K /mnt xorg gnome sushi pipewire pipewire-pulse pipewire-alsa pipewire-jack wireplumber noto-fonts noto-fonts-cjk noto-fonts-emoji noto-fonts-extra ttf-nerd-fonts-symbols-common power-profiles-deamon cups cups-pdf
arch-chroot /mnt systemctl enable gdm

echo "-- Removing Overlay mounts for System and Desktop --"
umount /mnt/usr
umount /mnt/var
umount /mnt/opt

echo "-- Creating Overlay mounts for System, Desktop and Data --"
mount -t overlay overlay -o lowerdir=/mnt/Shards/System/usr:/mnt/Shards/Desktop/usr,upperdir=/mnt/Shards/Data/usr,workdir=/mnt/Shards/Data/tmp/usr /mnt/usr
mount -t overlay overlay -o lowerdir=/mnt/Shards/System/var:/mnt/Shards/Desktop/var,upperdir=/mnt/Shards/Data/var,workdir=/mnt/Shards/Data/tmp/var /mnt/var
mount -t overlay overlay -o lowerdir=/mnt/Shards/System/opt:/mnt/Shards/Desktop/opt,upperdir=/mnt/Shards/Data/opt,workdir=/mnt/Shards/Data/tmp/opt /mnt/opt
