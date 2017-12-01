#!/usr/bin/env python
file = open('puzzle_input', 'r')
puzzle_input = file.read()
file.close()

count = 0

for index, value in enumerate(puzzle_input):
    if index == puzzle_input.__len__() - 1:
        if int(value) == int(puzzle_input[0]):
            count += int(value)
        break
    else:
        if int(value) == int(puzzle_input[index + 1]):
            count += int(value)
print(str(count))