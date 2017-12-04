#!/usr/bin/env python
file = open('puzzle_input', 'r')
puzzle_input = file.read()
file.close()
puzzle_input_lines = puzzle_input.split('\n')
sum = 0
line_correct = {}
i = 0
for line in puzzle_input_lines:
    i += 1
    words = {}
    line_correct[i] = True
    values = line.split(' ')
    for value in values:
        for word in words:
            if sorted(words[word]) == sorted(value):
                line_correct[i] = False
                break
        words[value] = value

for key in line_correct:
    if line_correct[key] == True:
        sum += 1

print(sum)
