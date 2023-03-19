#!/usr/bin/bash
set -e
set -x

sleep 2
exit 0

echo "-- Creating bind mount from /Shards/Data/etc to /Shards/System/etc"
mount --bind /mnt/Shards/Data/etc /mnt/Shards/System/etc

echo "-- Installing System Shard --"
pacstrap -K /mnt base linux linux-firmware networkmanager btrfs-progs grub efibootmgr systemd-sysvcompat man-db man-pages texinfo nano sudo curl archlinux-keyring which base-devel bash-completion zsh-completions bluez podman
arch-chrot /mnt systemctl enable NetworkManager
arch-chroot /mnt systemctl enable bluetooth
sed -i 's/MODULES=()/MODULES=(overlay)/g' /mnt/etc/mkinitcpio.conf
arch-chroot /mnt mkinitcpio -P

echo "-- Removing bind mount from /Shards/Data/etc to /Shards/System/etc"
umount /mnt/Shards/System/etc
