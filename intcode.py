#!/bin/env python

inputFile = open('./program', 'r')

program = [int(i) for i in inputFile.read().strip().split(',')]


i = 0

#program = [1101,100,-1,4,0]
#print(','.join(str(i) for i in program))

#program = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

#program = [3,9,8,9,10,9,4,9,99,-1,8]
#program = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
#program = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]

while program[i] != 99:
#    print("Index: {}".format(i))
    n = str(program[i]);
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
        program[ program[i+1] ] = input()
        i += 2

    elif instruction == 4:
        print(arg1)
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

#print(','.join(str(i) for i in program))
#print(program)

inputFile.close()

