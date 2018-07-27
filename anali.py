#!/usr/bin/python27

import argparse
import subprocess

from subprocess import run

parser = argparse.ArgumentParser(description='6tisch result file analizer')
parser.add_argument('--mother directory for everything', type=int, help='')
args = parser.parse_args()

#for now we try to plot everything we find in files!

command = ''
return_code = subprocess.run(command, shell=True, stdout=subprocess.PIPE, timeout=400)
result = return_code.stdout.decode()