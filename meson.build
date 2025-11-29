project('purelib-and-platlib', ['c', 'cpp'],
default_options : ['c_std=c11', 'cpp_std=c++14'])
add_global_arguments('-DKS_STR_ENCODING_NONE', language : 'cpp')

# libvorbis_dep = dependency('vorbis', version : '>=1.3.6')
# libogg_dep = dependency('ogg', version : '>=1.3.4')

py = import('python').find_installation(pure: false)

py.install_sources(
    ['wem2ogg-stubs/__init__.pyi'],
    subdir: 'wem2ogg-stubs'
)

py.extension_module(
    'wem2ogg',
    'wem2ogg.cpp',
    'wwise-audio-tools/src/ww2ogg/codebook.cpp',
    'wwise-audio-tools/src/ww2ogg/crc.c',
    'wwise-audio-tools/src/ww2ogg/ww2ogg.cpp',
    'wwise-audio-tools/src/ww2ogg/wwriff.cpp',
    'wwise-audio-tools/src/revorb/revorb.cpp',
    'wwise-audio-tools/src/wwtools/wwtools.cpp',
    'wwise-audio-tools/src/wwtools/w3sc.cpp',
    'wwise-audio-tools/src/wwtools/bnk.cpp',
    'wwise-audio-tools/src/kaitai/kaitaistream.cpp',
    'wwise-audio-tools/src/kaitai/structs/bnk.cpp',
    'wwise-audio-tools/src/kaitai/structs/vlq.cpp',
    'wwise-audio-tools/src/kaitai/structs/w3sc.cpp',
    'wwise-audio-tools/src/kaitai/structs/wem.cpp',
    #'wwise-audio-tools/src/ww2ogg/packed_codebooks.cpp',
    'wwise-audio-tools/src/ww2ogg/packed_codebooks_aoTuV_603.cpp',
    'wwise-audio-tools/libogg/src/bitwise.c',
    'wwise-audio-tools/libogg/src/framing.c',
    'wwise-audio-tools/libogg/src/crctable.h',
    'wwise-audio-tools/libvorbis/lib/mdct.c',
    'wwise-audio-tools/libvorbis/lib/smallft.c',
    'wwise-audio-tools/libvorbis/lib/block.c',
    'wwise-audio-tools/libvorbis/lib/envelope.c',
    'wwise-audio-tools/libvorbis/lib/window.c',
    'wwise-audio-tools/libvorbis/lib/lsp.c',
    'wwise-audio-tools/libvorbis/lib/lpc.c',
    'wwise-audio-tools/libvorbis/lib/analysis.c',
    'wwise-audio-tools/libvorbis/lib/synthesis.c',
    'wwise-audio-tools/libvorbis/lib/psy.c',
    'wwise-audio-tools/libvorbis/lib/info.c',
    'wwise-audio-tools/libvorbis/lib/floor1.c',
    'wwise-audio-tools/libvorbis/lib/floor0.c',
    'wwise-audio-tools/libvorbis/lib/res0.c',
    'wwise-audio-tools/libvorbis/lib/mapping0.c',
    'wwise-audio-tools/libvorbis/lib/registry.c',
    'wwise-audio-tools/libvorbis/lib/codebook.c',
    'wwise-audio-tools/libvorbis/lib/sharedbook.c',
    'wwise-audio-tools/libvorbis/lib/lookup.c',
    'wwise-audio-tools/libvorbis/lib/bitrate.c',
    #dependencies: [libvorbis_dep, libogg_dep],
    install: true,
    #install_dir: py.get_install_dir() / 'wem2ogg'
    include_directories : include_directories('wwise-audio-tools/include'),
)
