pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
upgradewindowsdir = join_paths(pkgdatadir, 'shard_updater/windows/UpgradeWindows')

shard_updater_sources = [
    '__init__.py',
    'Upgrade.py',
    'UpgradeFail.py',
    'UpgradeFinish.py'
]
install_data(shard_updater_sources, install_dir: upgradewindowsdir)
