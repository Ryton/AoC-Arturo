#!/usr/bin/env python3

from json import loads
from functools import cmp_to_key


def compare(a, b):
	a_is_int = type(a) is int
	b_is_int = type(b) is int

	if a_is_int and b_is_int:
		return a - b

	if a_is_int ^ b_is_int:
		return compare([a], b) if a_is_int else compare(a, [b])

	for x, y in zip(a, b):
		res = compare(x, y)
		if res != 0:
			return res

	return len(a) - len(b)

fin =open('C:\\Users\\joachim.verhelst\\.config\\aocd\\github.Ryton.1321098\\2022_13_input.txt')
with fin:
	lines = fin.read().replace('\n\n', '\n').splitlines()

packets = list(map(loads, lines))
pairs   = (packets[i:i + 2] for i in range(0, len(packets), 2))
answer  = sum(i for i, p in enumerate(pairs, 1) if compare(*p) < 0)

print('1:', answer)


packets.extend(([[2]], [[6]]))
packets.sort(key=cmp_to_key(compare))

answer = packets.index([[2]]) + 1
answer *= packets.index([[6]], answer) + 1
print('2:', answer)
