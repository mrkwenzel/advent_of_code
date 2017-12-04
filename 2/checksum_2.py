#!/usr/bin/env python
file = open('puzzle_input', 'r')
puzzle_input = file.read()
file.close()
puzzle_input_lines = puzzle_input.split('\n')
sum = 0
for line in puzzle_input_lines:
    values = line.split(';')
    for key, value in enumerate(values):
        for inner_key, inner_value in enumerate(values):
            out_value = int(value)
            in_value = int(inner_value)
            if inner_key is not key and out_value != 0 and in_value != 0:
                diff = out_value / in_value
                if diff.is_integer():
                    sum += diff
                    break
print(sum)