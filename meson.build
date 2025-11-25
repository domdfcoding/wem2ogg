project('purelib-and-platlib', 'cpp',
default_options : ['c_std=c11', 'cpp_std=c++14'])

py = import('python').find_installation(pure: false)

py.install_sources(
    ['misc/__init__.py', 'misc/py.typed', 'wem2ogg.pyi'],
    subdir: 'wem2ogg'
)

py.extension_module(
    'wem2ogg',
    'wem2ogg.cpp',
    install: true,
    install_dir: py.get_install_dir() / 'wem2ogg'
)
