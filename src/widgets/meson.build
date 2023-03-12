pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
widgetsdir = join_paths(pkgdatadir, 'shard_updater/widgets')

shard_updater_sources = [
    '__init__.py',
    'MenuButton.py',
    'Disk.py'
]
install_data(shard_updater_sources, install_dir: widgetsdir)
