#!/usr/bin/bash
set -x


SSD=""
lsblk -d -o ROTA /dev/disk/by-label/SHARDS | grep -q 0
if [[ $? -eq 0 ]]; then
    SSD="ssd,"
fi

set -e

echo "-- Mounting Root shard to /mnt --"
mount /dev/disk/by-label/SHARDS /mnt -o subvol=Root

echo "-- Installing Root preloader --"
pacstrap -K /mnt base
touch /mnt/init
cat > /mnt/init <<EOF
#!/usr/bin/bash
echo -e "\\x1b[35;1m --STARTING PROJECT SHARD STAGE 1-- \\x1b[39m"
echo "Mounting Shards"
mount /dev/disk/by-label/SHARDS -t btrfs -o rw,${SSD}relatime,space_cache=v2,compress,subvol=Data /Shards/Data
mount /dev/disk/by-label/SHARDS -t btrfs -o rw,${SSD}relatime,space_cache=v2,compress,subvol=Desktop /Shards/Desktop
mount /dev/disk/by-label/SHARDS -t btrfs -o rw,${SSD}relatime,space_cache=v2,compress,subvol=System /Shards/System
mount /dev/disk/by-label/SHARDS -t btrfs -o rw,${SSD}relatime,space_cache=v2,compress,subvol=Users /Shards/Users
echo "Creating overlays"
mount -t overlay overlay -o lowerdir=/Shards/System/opt:/Shards/Desktop/opt,upperdir=/Shards/Data/opt,workdir=/Shards/Data/tmp/opt /opt
mount -t overlay overlay -o lowerdir=/Shards/System/usr:/Shards/Desktop/usr,upperdir=/Shards/Data/usr,workdir=/Shards/Data/tmp/usr /usr
mount -t overlay overlay -o lowerdir=/Shards/System/var:/Shards/Desktop/var,upperdir=/Shards/Data/var,workdir=/Shards/Data/tmp/var /var
echo "Mounting bind mounts"
mount --bind /Shards/System/boot /boot
mount --bind /Shards/Users /home
mount --bind /Shards/Data/etc /etc
echo -e "\\x1b[35;1m --STARTING PROJECT SHARD STAGE 2-- \\x1b[39m"
exec /Shards/System/sbin/init
EOF
chmod +x /mnt/init

# for some reason gpg-agent continues running, so we have to find the pid with lsof and kill it
echo "-- Stopping gpg-agent --"
set +e
gpg_pid_agent=$(lsof -t +D /mnt/etc/pacman.d/gnupg/)
kill ${gpg_agent_pid}
gpg_agent_pid=$(lsof -t +D /mnt/etc/pacman.d/gnupg/)
kill ${gpg_agent_pid}
set -e

echo "-- Mounting Shards --"
mkdir -p /mnt/Shards/{Data,Desktop,System,Users}
mount /dev/disk/by-label/SHARDS -t btrfs -o rw,${SSD}relatime,space_cache=v2,compress,subvol=Data /mnt/Shards/Data
mount /dev/disk/by-label/SHARDS -t btrfs -o rw,${SSD}relatime,space_cache=v2,compress,subvol=Desktop /mnt/Shards/Desktop
mount /dev/disk/by-label/SHARDS -t btrfs -o rw,${SSD}relatime,space_cache=v2,compress,subvol=System /mnt/Shards/System
mount /dev/disk/by-label/SHARDS -t btrfs -o rw,${SSD}relatime,space_cache=v2,compress,subvol=Users /mnt/Shards/Users
