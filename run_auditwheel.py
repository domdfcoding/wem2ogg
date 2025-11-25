#! /usr/bin/env python

# stdlib
import os
import subprocess
from pathlib import Path

files = [p for p in Path("dist").glob("*.whl") if "manylinux" not in p.name]

env = os.environ.copy()
env["LD_LIBRARY_PATH"] = ':'.join([
		os.path.join(os.getcwd(), "wwise-audio-tools/build/lib"),
		os.getenv("LD_LIBRARY_PATH", ''),
		])
print(subprocess.check_output(["auditwheel", "repair", *files, "-w", "dist"], env=env))

for file in files:
	file.unlink()
