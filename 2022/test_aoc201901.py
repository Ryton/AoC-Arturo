# test_aoc201901.py


import pathlib

import pytest

import aoc_solution_template as aoc

day = 1
year = 2022

@pytest.fixture
def example1():

    iE = ("C:\\Users\\joachim.verhelst\\.config\\aocd\\github.Ryton.1321098\\",str(year),"_", str(day),"_example_input.txt").read_text().strip()


    return iE


@pytest.fixture
def example2():
    iA = ("C:\\Users\\joachim.verhelst\\.config\\aocd\\github.Ryton.1321098\\", str(year), "_", str(day),
          "_input.txt").read_text().strip()
    return iA

def test_parse_example1(example1):

    """Test that input is parsed properly."""

    assert example1[0:9] == 'v...>>.vv>'

def test_part1_example1(example1):

    """Test part 1 on example input."""

    assert aoc.part1(example1) == 2 + 2 + 654 + 33583



def test_part2_example1(example1):

    """Test part 2 on example input."""

    assert aoc.part2(example1) == "test"


@pytest.mark.skip(reason="Not implemented")

def test_part2_example2(example2):

    """Test part 2 on example input."""

    assert aoc.part2(example2) == ...