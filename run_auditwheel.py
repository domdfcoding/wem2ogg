#! /usr/bin/env python

# stdlib
import os
import platform
import subprocess
from pathlib import Path

files = [p for p in Path("dist").glob("*.whl") if "manylinux" not in p.name]

env = os.environ.copy()

if platform.system() == "Linux":
	command = "auditwheel"
elif platform.system() == "Windows":
	command = "delvewheel"
else:
	sys.exit()

subprocess.check_output([command, "repair", *files, "-w", "dist"], env=env)

if platform.system() == "Linux":
	for file in files:
		file.unlink()
