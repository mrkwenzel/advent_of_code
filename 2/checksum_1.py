#!/usr/bin/env python
file = open('puzzle_input', 'r')
puzzle_input = file.read()
file.close()
puzzle_input_lines = puzzle_input.split('\n')
sum = 0
for line in puzzle_input_lines:
    values = line.split(';')
    values = map(int, values)
    max_value = max(values)
    values = line.split(';')
    values = map(int, values)
    min_value = min(values)
    diff = max_value - min_value
    sum += diff

print(sum)