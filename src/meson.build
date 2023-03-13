pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'shard_updater')
gnome = import('gnome')

gnome.compile_resources('shard_updater',
  'shard_updater.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'shard_updater.in',
  output: 'shard_updater',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

shard_updater_sources = [
  '__init__.py',
  'main.py',
  'window.py',
  'HeaderBar.py'
]

install_data(shard_updater_sources, install_dir: moduledir)
subdir('windows')
subdir('widgets')
subdir('utils')
