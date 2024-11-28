# aoc_solution_template.py

import pathlib
import sys

#!pip install advent-of-code-data
#https://github.com/wimglenn/advent-of-code-data #for input parsing/loading
#from aocd import get_data # simple
from aocd.models import Puzzle

def grab_input(day=25,year=2022):
    puzzle = Puzzle(year=year, day=day)
    #print(puzzle.user)
    #print(puzzle.input_data_fname)
    iE = puzzle.example_data
    iA = puzzle.input_data
    return iE,iA

def parse(i):
    """Parse input."""
    pass

def part1(data):
    print(iA_p,iE_p)
    """Solve part 1."""
    return 2 + 2 + 654 + 33583

def part2(data):
    return "test"
    """Solve part 2."""


def solve(puzzle_input):

    """Solve the puzzle for the given input."""

    data = parse(puzzle_input)

    solution1 = part1(data)

    solution2 = part2(data)


    return solution1, solution2


if __name__ == "__main__":
        iE,iA =grab_input()
        solutions = solve(puzzle_input)

        print("\n".join(str(solution) for solution in solutions))