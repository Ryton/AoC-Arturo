#!/usr/bin/python3

#use example $" python ./input_parser.py --day 6 > 6.txt"

import argparse
import subprocess
import sys

SESSION = '53616c7465645f5ff36c6b3408118ba047f7d2283bf1efd9cf836e33042e5d93dbdaa7327392dde19a638cd1a16cebd6'
parser = argparse.ArgumentParser(description="Read input")
parser.add_argument("--year", type=int, default=2021)
parser.add_argument("--day", type=int, default=6)
args = parser.parse_args()

cmd = 'curl https://adventofcode.com/{}/day/{}/input --cookie "session={}"'.format(
    args.year, args.day, SESSION
)
output = subprocess.check_output(cmd, shell=True)
output = output.decode("utf-8")
print(output, end="")
print("\n".join(output.split("\n")[:10]), file=sys.stderr)