pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
installwindowsdir = join_paths(pkgdatadir, 'shard_updater/windows/InstallWindows')

shard_updater_sources = [
    '__init__.py',
    'InstallProgress.py',
    'DiskSelect.py',
    'InstallFail.py',
    'InstallFinish.py'
]
install_data(shard_updater_sources, install_dir: installwindowsdir)
