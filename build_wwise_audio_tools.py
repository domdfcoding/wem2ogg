#! /usr/bin/env python
# stdlib
import os
import subprocess

os.chdir("wwise-audio-tools")
subprocess.run(["cmake", "-B", "build", "-DCMAKE_POLICY_VERSION_MINIMUM=3.5"], check=False)
subprocess.run(["cmake", "--build", "build"], check=False)
