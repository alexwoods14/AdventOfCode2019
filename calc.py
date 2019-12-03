#!/bin/env python

inputFile = open('./program', 'r')

program = [int(i) for i in inputFile.read().strip().split(',')]


i = 0

while program[i] != 99:
    if program[i] == 1: # add
        program[ program[i+3] ] = program[ program[i+1] ] + program[ program[i+2] ]

    elif program[i] == 2: # multiply
        program[ program[i+3] ] = program[ program[i+1] ] * program[ program[i+2] ]

    i += 4

#print(','.join(str(i) for i in program))
print(program[0])

inputFile.close()
