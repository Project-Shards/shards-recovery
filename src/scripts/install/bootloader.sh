#!/usr/bin/bash
set -e
set -x

sleep 2
exit 0

arch-chroot /mnt grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=SHARDS_SYSTEM
arch-chroot /mnt grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=SHARDS_SYSTEM --removable

sed -i 's|quiet|quiet init=/init|g' /mnt/etc/default/grub
arch-chroot /mnt grub-mkconfig -o /boot/grub/grub.cfg
