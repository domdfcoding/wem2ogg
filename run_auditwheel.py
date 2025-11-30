#! /usr/bin/env python

# stdlib
import os
import subprocess
from pathlib import Path

files = [p for p in Path("dist").glob("*.whl") if "manylinux" not in p.name]

env = os.environ.copy()
subprocess.check_output(["auditwheel", "repair", *files, "-w", "dist"], env=env)

for file in files:
	file.unlink()
