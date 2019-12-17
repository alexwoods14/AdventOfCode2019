#!/bin/env python

minimum = 109165
maximum = 576723

current = minimum
possible = 0

def isValid(password):
    pw = str(password)

    current = []

    last = None
    hasDouble = False

    prev = None
    length = 0

    for c in pw: # check order
        if last != None and c < last:
            return False
        last = c


    for i in range (0, 6):
        if pw[i] == prev:
            length += 1
        else:
            if length == 2:
                return True
            length = 1

        prev = pw[i]


    if length == 2:
        return True

    return False



#        if pw[i] == pw[i+1]:
#            if pw[i] != pw[i+2]:
#                hasDouble = True
#        elif i == 3 and pw[i+1] == pw[i+2]:
#            hasDouble = True

    return hasDouble


#print(isValid(111111))
#print("111122 T- ",isValid(111122))
#print("122789 T- ",isValid(122789))
#print("222289 F- ",isValid(222289))
#print("123369 T- ",isValid(123369))
#print("133369 F- ",isValid(133369))

while current < maximum:
    if isValid(current):
        possible += 1

    current += 1

print(possible)

