#!/usr/bin/env python
file = open('puzzle_input', 'r')
puzzle_input = file.read()
file.close()
puzzle_input_lines = puzzle_input.split('\n')

steps = 0
current_step = 0

while True:
    try:
        next_step = current_step + int(puzzle_input_lines[current_step])
        puzzle_input_lines[current_step] = int(puzzle_input_lines[current_step]) + 1
        current_step = next_step
        steps += 1
    except IndexError:
        break

print(steps)
