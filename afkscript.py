#!/usr/bin/python3
#A script that continually enters LS to prevent automatic logouts (Example: SSH sessions)
import time
import sys
from subprocess import PIPE, Popen

def cmdline(command):
    process = Popen(
            args=command,
            stdout=PIPE,
            shell=True,
            universal_newlines=True
    )
    return process.communicate()[0]

cmd_output = cmdline('ls -alr').rstrip()

while True:
    print(cmd_output)
    time.sleep(60)
