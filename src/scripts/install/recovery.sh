#!/usr/bin/bash
set -e
set -x


echo "-- Mounting partitions --"
mount /dev/disk/by-label/SHARDS /mnt -o subvol=Recovery
mkdir -p /mnt/boot/efi
mount /dev/disk/by-label/SHARDSEFI /mnt/boot/efi

echo "-- Installing Recovery Shard --"
pacstrap -K /mnt base linux linux-firmware networkmanager btrfs-progs grub efibootmgr systemd-sysvcompat man-db man-pages texinfo nano sudo curl arch-install-scripts archlinux-keyring which base-devel bash-completion zsh-completions gparted ntfs-3g dosfstools exfat-utils openssh
genfstab -U /mnt >> /mnt/etc/fstab
arch-chroot /mnt /bin/bash -c "systemctl enable NetworkManager"
arch-chroot /mnt /bin/bash -c "systemctl enable sshd"

echo "-- Setting up user --"
arch-chroot /mnt useradd -m -p "$(openssl passwd -1 "shards")" -s /bin/bash shards
arch-chroot /mnt usermod -aG wheel shards
sed 's/# %wheel ALL=(ALL) ALL/%wheel ALL=(ALL) ALL/g' /mnt/etc/sudoers
echo "Defaults pwfeedback" >> /mnt/etc/sudoers
mkdir -p /mnt/etc/systemd/system/getty@tty1.service.d/
touch /mnt/etc/systemd/system/getty@tty1.service.d/autologin.conf
echo "[Service]" >> /mnt/etc/systemd/system/getty@tty1.service.d/autologin.conf
cat  > /mnt/etc/systemd/system/getty@tty1.service.d/autologin.conf << EOF
[Service]
ExecStart=
ExecStart=-/usr/bin/agetty -o '-p -f -- \\u' --autologin recovery --noclear shards %I \$TERM
EOF


echo "-- Installing GRUB --"
arch-chroot /mnt grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=SHARDS_RECOVERY
arch-chroot /mnt grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=SHARDS_RECOVERY --removable
arch-chroot /mnt grub-mkconfig -o /boot/grub/grub.cfg

# for some reason gpg-agent continues running, so we have to find the pid with lsof and kill it
echo "-- Stopping gpg-agent --"
set +e
gpg_agent_pid=$(lsof -t +D /mnt/etc/pacman.d/gnupg/)
kill "${gpg_agent_pid}"
set -e

echo "-- Unmounting partitions --"
umount -R /mnt
