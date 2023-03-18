pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
updatedatadir = join_paths(pkgdatadir, 'shard_updater/scripts/upgrade/data')

shard_updater_sources = [
    'mount.sh',
    'snapshot.sh',
    'update.sh'
]
install_data(shard_updater_sources, install_dir: updatedatadir)
