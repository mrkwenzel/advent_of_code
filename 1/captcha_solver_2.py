#!/usr/bin/env python
file = open('puzzle_input', 'r')
puzzle_input = file.read()
file.close()

count = 0

for index, value in enumerate(puzzle_input):
    next_index = (puzzle_input.__len__() / 2) + index
    if next_index > puzzle_input.__len__() - 1:
        next_index = next_index - puzzle_input.__len__()
    if int(value) == int(puzzle_input[int(next_index)]):
        count += int(value)

print(str(count))