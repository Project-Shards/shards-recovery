pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
windowsdir = join_paths(pkgdatadir, 'shard_updater/windows')

shard_updater_sources = [
    '__init__.py',
    'RecoveryTerminalWindow.py',
    'InstallWindow.py'
]
install_data(shard_updater_sources, install_dir: windowsdir)

subdir('InstallWindows')
