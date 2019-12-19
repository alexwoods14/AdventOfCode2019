#!/bin/env python

from itertools import permutations

inputFile = open('./program', 'r')

program = [int(i) for i in inputFile.read().strip().split(',')]

inputFile.close()


#program = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
program = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]

def run(inputs, program):
    inputIndex = 0
    output = 0
    i = 0

    while program[i] != 99:
    #    print("Index: {}".format(i))
        n = str(program[i])
        instruction = int(n[-2:])
        arg1 = 0
        arg2 = 0
    
        if len(n) > 2 and n[-3] == "1":
            arg1 = program[i + 1]
        else:
            arg1 = program[ program[i + 1] ]
        
        if len(n) > 3 and n[-4] == "1" and instruction != 3 and instruction != 4:
            arg2 = program[i + 2]
        else:
    #        print("HERE")
    #        print(n) # 104
    #        print(i) # 10
    #        print(program[i + 2]) #1101
    #        print(len(program)) #678
            if instruction != 3 and instruction != 4:
                arg2 = program[ program[i + 2] ]
    
        # instruction
        arg1 = int(arg1)
        arg2 = int(arg2)
    
    
        if instruction == 1: # add
            program[ program[i+3] ] = arg1 + arg2
            i += 4
    
        elif instruction == 2: # multiply
            program[ program[i+3] ] = arg1 * arg2
            i += 4
    
        elif instruction == 3: # input
    #        print(i)
            #program[ program[i+1] ] = input()
            print(inputIndex)
            program[ program[i+1] ] = inputs[inputIndex]
            inputIndex += 1 

            i += 2
    
        elif instruction == 4: # output
            #print(arg1)
            output = arg1
            i += 2
            
        elif instruction == 5:
            if arg1 != 0:
                i = arg2
            else:
                i += 3
    
        elif instruction == 6:
            if arg1 == 0:
                i = arg2
            else:
                i += 3
    
        elif instruction == 7:
            if arg1 < arg2:
                program[ program[i+3] ] = 1
            else:
                program[ program[i+3] ] = 0
    
            i+=4
    
        elif instruction == 8:
            if arg1 == arg2:
                program[ program[i+3] ] = 1
            else:
                program[ program[i+3] ] = 0
    
            i+=4
    return output

#print(','.join(str(i) for i in program))
#print(program)

def runSequence(sequence, program):
    nextIn = 0
    print(sequence)
    for i in sequence:
        nextIn = run([i, nextIn], program.copy())

    return nextIn

def allPermutations(program):
    perms = list(permutations(range(5),5))
    maxi = 0
    highestPerm = None
    for i in perms:
        result = runSequence(i, program)
        print(i)
        if result > maxi:
            maxi = result
            highestPerm = i

    return maxi, highestPerm

maxi, highestPerm = allPermutations(program)

print("{} with sequence {}".format(maxi, highestPerm))
