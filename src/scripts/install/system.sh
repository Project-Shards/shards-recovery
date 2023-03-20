#!/usr/bin/bash
set -e
set -x


echo "-- Creating bind mount from /Shards/Data/etc to /Shards/System/etc"
mkdir -p /mnt/Shards/System/etc
mount --bind /mnt/Shards/Data/etc /mnt/Shards/System/etc

echo "-- Installing System Shard --"
pacstrap -K /mnt/Shards/System base linux linux-firmware networkmanager btrfs-progs grub efibootmgr systemd-sysvcompat man-db man-pages texinfo nano sudo curl archlinux-keyring which base-devel bash-completion zsh-completions bluez podman
arch-chroot /mnt/Shards/System systemctl enable NetworkManager
arch-chroot /mnt/Shards/System systemctl enable bluetooth
sed -i 's/MODULES=()/MODULES=(overlay)/g' /mnt/Shards/System/etc/mkinitcpio.conf
arch-chroot /mnt/Shards/System mkinitcpio -P

# for some reason gpg-agent continues running, so we have to find the pid with lsof and kill it
echo "-- Stopping gpg-agent --"
set +e
gpg_agent_pid=$(lsof -t +D /mnt/Shards/System/etc/pacman.d/gnupg/)
kill ${gpg_agent_pid}
gpg_agent_pid=$(lsof -t +D /mnt/Shards/System/etc/pacman.d/gnupg/)
kill ${gpg_agent_pid}
set -e

echo "-- Removing bind mount from /Shards/Data/etc to /Shards/System/etc"
umount /mnt/Shards/System/etc
