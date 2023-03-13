pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
utilsdir = join_paths(pkgdatadir, 'shard_updater/utils')

shard_updater_sources = [
    '__init__.py',
    'threading.py',
]
install_data(shard_updater_sources, install_dir: utilsdir)
