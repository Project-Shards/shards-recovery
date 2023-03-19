pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
installscriptsdir = join_paths(pkgdatadir, 'shard_updater/scripts/install/')

shard_updater_sources = [
    'data.sh',
    'desktop.sh',
    'recovery.sh',
    'root.sh',
    'system.sh',
    'bootloader.sh'
]
install_data(shard_updater_sources, install_dir: installscriptsdir)
subdir('partition')
