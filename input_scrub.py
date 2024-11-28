#!/usr/bin/python3

#use example $" python ./input_scrub.py --day 6 > 6.txt"
#use example 2 $"import input_scrub.  input_scrub.parse_from_url(day=6,filename)"


import argparse
import subprocess
import sys

SESSION = '53616c7465645f5ff36c6b3408118ba047f7d2283bf1efd9cf836e33042e5d93dbdaa7327392dde19a638cd1a16cebd6'


def dump_output_in_file(output = None, filename=None):
    if filename ==None:
        filename='input.txt'
    if output==None:
        print('please provide parser input file')
        return 0

    with open(filename, 'a') as f:
        f.write(output+"")
        #f.write("\n".join(output.split("\n")[:10]))
        print('succes!')
        #f.write(file=sys.stderr)
        #print(output, end="")
        #print()

def parse_from_URL(day=None,year=2021,filename=None):
    cmd = 'curl https://adventofcode.com/{}/day/{}/input --cookie "session={}"'.format(
        year, day, SESSION
    )
    if filename ==None:
        filename=str(day)+'.txt'

    output = subprocess.check_output(cmd, shell=True)
    output = output.decode("utf-8")

    with open(filename, 'a') as f:
        f.write(output+"")
        f.write("\n".join(output.split("\n")[:10]))
        #f.write(file=sys.stderr)
        #print(output, end="")
        #print()

if __name__=='__main__':
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