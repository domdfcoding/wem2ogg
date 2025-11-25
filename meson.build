project('purelib-and-platlib', ['c', 'cpp'],
default_options : ['c_std=c11', 'cpp_std=c++14'])

r = run_command('python3', 'build_wwise_audio_tools.py')
output = r.stdout().strip()
errortxt = r.stderr().strip()
message('@0@'.format(errortxt))


py = import('python').find_installation(pure: false)

dir_base = meson.current_source_dir()
cc = meson.get_compiler('cpp')
wwise = cc.find_library('wwtools', dirs: join_paths(dir_base, 'wwise-audio-tools/build/lib'))

#py.install_sources(
#    ['misc/__init__.py', 'misc/py.typed', 'wem2ogg.pyi'],
#    subdir: 'wem2ogg'
#)

py.extension_module(
    'wem2ogg',
    'wem2ogg.cpp',
    dependencies: wwise,
    install: true,
    #install_dir: py.get_install_dir() / 'wem2ogg'
    include_directories : include_directories('wwise-audio-tools/include'),
)
