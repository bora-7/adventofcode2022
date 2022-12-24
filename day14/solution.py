from collections import deque
from collections import defaultdict
import ast
import heapq
import string
from functools import cmp_to_key

# sand is pouring from (500,0)
# first build the matrix, mark all the coordinates blocked by rocks
# then start sending the sand, count until a sand reaches the below boundaries of the matrix
# return count
def partOneSolution():
    sandCount = 0
    paths = []
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip()
            line = line.split(' -> ')
            paths.append(line)

    #print(paths)
    # now to initialise the 2D Matrix map, find the biggest Y and X coordinates 
    # INSTEAD OF USING A 2D ARRAY, USE A SET 

    biggestX = 0
    biggestY = 0
    filled = set()
    for path in paths:
        for num in path:
            x, y = num.split(',')
            biggestX = max(biggestX, int(x))
            biggestY = max(biggestY, int(y))

    
    # now populate the map with the rocks
    for path in paths:
        prevCoordinate = None
        for num in path:
            x, y = num.split(',')
            x = int(x)
            y = int(y)
            if prevCoordinate != None:
                if prevCoordinate[0] == x:
                    for i in range(min(prevCoordinate[1], y), max(prevCoordinate[1], y)+1):
                        filled.add((x, i))
                else: 
                    for i in range(min(prevCoordinate[0], x), max(prevCoordinate[0], x)+1):
                        filled.add((i, y))
            
            prevCoordinate = [x, y]
    
    # start sending the sand from (500, 0)
    # do this in a while loop with the only way to break out being a sand reaching the bottom

    def simulateSand():
        sandX, sandY = 500, 0

        while sandY <= biggestY:
            if (sandX, sandY+1) not in filled:
                sandY += 1
                continue

            if (sandX-1, sandY+1) not in filled:
                sandY += 1
                sandX -= 1
                continue

            if (sandX+1, sandY+1) not in filled:
                sandY += 1
                sandX += 1
                continue
        
            filled.add((sandX, sandY))
            return True
        
        return False
    
    while True:
        x = simulateSand()
        
        if x == False:
            return sandCount
        
        sandCount += 1


def partTwoSolution():
    sandCount = 0
    paths = []
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip()
            line = line.split(' -> ')
            paths.append(line)

    #print(paths)
    # now to initialise the 2D Matrix map, find the biggest Y and X coordinates 
    # INSTEAD OF USING A 2D ARRAY, USE A SET 

    biggestX = 0
    biggestY = 0
    filled = set()
    for path in paths:
        for num in path:
            x, y = num.split(',')
            biggestX = max(biggestX, int(x))
            biggestY = max(biggestY, int(y))

    
    # now populate the map with the rocks
    for path in paths:
        prevCoordinate = None
        for num in path:
            x, y = num.split(',')
            x = int(x)
            y = int(y)
            if prevCoordinate != None:
                if prevCoordinate[0] == x:
                    for i in range(min(prevCoordinate[1], y), max(prevCoordinate[1], y)+1):
                        filled.add((x, i))
                else: 
                    for i in range(min(prevCoordinate[0], x), max(prevCoordinate[0], x)+1):
                        filled.add((i, y))
            
            prevCoordinate = [x, y]
    
    # start sending the sand from (500, 0)
    # do this in a while loop with the only way to break out being a sand reaching the bottom

    def simulateSand():
        sandX, sandY = 500, 0

        if (sandX, sandY) in filled:
            return (sandX, sandY)
        
        while sandY <= biggestY:
            if (sandX, sandY+1) not in filled:
                sandY += 1
                continue

            if (sandX-1, sandY+1) not in filled:
                sandY += 1
                sandX -= 1
                continue

            if (sandX+1, sandY+1) not in filled:
                sandY += 1
                sandX += 1
                continue
        
            break
        
        return (sandX, sandY)
    
    while True:
        x, y = simulateSand()
        
        filled.add((x, y))
        sandCount += 1
        if (x, y) == (500, 0):
            return sandCount

def main():
    print(partOneSolution())
    print(partTwoSolution())

main()