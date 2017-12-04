#!/usr/bin/env python
import math

value = 0

# Method found on https://gist.github.com/hazpotts/ac0b6f872600ceb7f95d

def calc(id):
    if id == 1:
        x = 0
        y = 0
    else :
        idSqrt = math.sqrt(id) #find the square root of the id
        lowSqrt = math.floor(idSqrt) #round the square root down
        highSqrt = math.ceil(idSqrt) #round the square root up
        if lowSqrt is highSqrt: #if they are the same it's the last position
            lowSqrt = lowSqrt - 2 #to calculate previous odd square root
        if lowSqrt % 2 == 0: #if in the second half of the ring the low root is even, need to find the previous odd because centered rings are odd number sided squares
            lowSqrt-=1
        if highSqrt % 2 == 0:#same but for first half and high root
            highSqrt+=1
        previousRingEnd = pow(lowSqrt, 2) #square root rounded down and then squared finds the number at the end of the previous ring
        ringEnd = pow(highSqrt, 2) #the same but for the end of the current ring
        ringPosition = id - previousRingEnd # (15-9 = 6) taking the previous ring from the id finds the position around the current ring
        ringTotal = ringEnd - previousRingEnd # (25-9 = 16) taking the previous ring from the current finds the total count around the current ring
        sideLengthMinusOne = ringTotal / 4 # 16/4 = 4
        halfSideLengthMO = sideLengthMinusOne / 2 # 4/2 = 2
        side = ringPosition/ringTotal

         # This calculates what side it's on
         # and it's position along that side.
         # Corner positions count as being the last on the side
         # hence the minus 1 on side length, because the first
         # corner of each side counted for the previous side.
         # Corners could be calculated from either side that they
         # are a part of.


        if side <= 0.25: # right hand side
            x = halfSideLengthMO
            y = halfSideLengthMO - ringPosition

        if side <= 0.5: # bottom
            x = halfSideLengthMO - (ringPosition - sideLengthMinusOne)
            y = -halfSideLengthMO

        if side <= 0.75: # left hand side
            x = -halfSideLengthMO
            y = -halfSideLengthMO + (ringPosition - (sideLengthMinusOne*2))

        if side > 0.75: # top
            x = -halfSideLengthMO + (ringPosition - (sideLengthMinusOne*3))
            y = halfSideLengthMO

        dist = math.fabs(0-x)+math.fabs(0-y)
        print(int(dist))

calc(value)
