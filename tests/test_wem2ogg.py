# 3rd party
from domdf_python_tools.paths import PathPlus

# this package
from wem2ogg import wem_to_ogg

data_dir = PathPlus(__file__).parent.parent / "wwise-audio-tools/tests/testdata/wem"
wem_file = data_dir / "test1.wem"
ogg_file = data_dir / "test1.ogg"


def test_conversion():
	wem_data = wem_file.read_bytes()
	ogg_data = wem_to_ogg(wem_data)
	assert len(ogg_data) == 1143628
	assert ogg_data == ogg_file.read_bytes()
