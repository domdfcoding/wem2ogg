#! /usr/bin/env python
# stdlib
import os
import subprocess

os.chdir("wwise-audio-tools")
subprocess.run(["cmake", "-B", "build"], check=False)
subprocess.run(["cmake", "--build", "build"], check=False)
