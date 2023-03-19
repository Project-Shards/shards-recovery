pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
partitionscriptsdir = join_paths(pkgdatadir, 'shard_updater/scripts/install/partition/')

shard_updater_sources = [
    'block.sh',
    'nvme.sh',
    'partition.sh',
    'shards.sh',
]
install_data(shard_updater_sources, install_dir: partitionscriptsdir)
