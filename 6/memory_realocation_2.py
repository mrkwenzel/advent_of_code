#!/usr/bin/env python
file = open('puzzle_input', 'r')
puzzle_input = file.read()
file.close()
puzzle_input_lines = puzzle_input.split('\t')

puzzle_input_lines = list(map(int, puzzle_input_lines))

markings = {}

markings[0] = list(puzzle_input_lines)

no_of_markings = 0

found_exact_marking = False

while True:
    bank_size = 0
    bank_index = 0
    for key in range(puzzle_input_lines.__len__()):
        if bank_size <= puzzle_input_lines[puzzle_input_lines.__len__() - key - 1]:
            bank_size = puzzle_input_lines[puzzle_input_lines.__len__() - key - 1]
            bank_index = puzzle_input_lines.__len__() - key - 1

    puzzle_input_lines[bank_index] = 0

    current_bank = bank_index
    for memory_available_steps in range(bank_size):
        current_bank += 1
        try:
            puzzle_input_lines[current_bank]
        except IndexError:
            current_bank = 0
        puzzle_input_lines[current_bank] += 1

    for index in markings:
        if markings[index] == puzzle_input_lines:
            found_exact_marking = True
            found_exact_marking_at_index = index
            break

    if found_exact_marking:
        no_of_markings += 1
        markings[no_of_markings] = list(puzzle_input_lines)
        break

    no_of_markings += 1
    markings[no_of_markings] = list(puzzle_input_lines)

print(no_of_markings - index)
