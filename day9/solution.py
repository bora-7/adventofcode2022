from collections import defaultdict


# need helper functions
# helper -> check if H is adjacent to T
# if not: helper -> move T one step so that it's adjacent to H

# to keep track of the locations that T visited, we can have a set storing tuples (coordinates)
# keep track of tail and head coordinates in separate lists, so we can modify them quickly

def isHeadAdjacent(tailCoordinate, headCoordinate):
    if abs(headCoordinate[0] - tailCoordinate[0]) > 1 or abs(headCoordinate[1] - tailCoordinate[1]) > 1:
        return False
    return True

def newTailCoordinate(tailCoordinate, headCoordinate):
    if abs(headCoordinate[0] - tailCoordinate[0]) == 0:
        if headCoordinate[1] > tailCoordinate[1]:
            return [tailCoordinate[0], tailCoordinate[1]+1]
        else:
            return [tailCoordinate[0], tailCoordinate[1]-1]
    elif abs(headCoordinate[1] - tailCoordinate[1]) == 0:
        if headCoordinate[0] > tailCoordinate[0]:
            return [tailCoordinate[0]+1, tailCoordinate[1]]
        else:
            return [tailCoordinate[0]-1, tailCoordinate[1]]
    else: # need to move diagnoally
        if headCoordinate[0] > tailCoordinate[0] and headCoordinate[1] > tailCoordinate[1]:
            return [tailCoordinate[0]+1, tailCoordinate[1]+1]
        elif headCoordinate[0] > tailCoordinate[0] and headCoordinate[1] < tailCoordinate[1]:
            return [tailCoordinate[0]+1, tailCoordinate[1]-1]
        elif headCoordinate[0] < tailCoordinate[0] and headCoordinate[1] > tailCoordinate[1]:
            return [tailCoordinate[0]-1, tailCoordinate[1]+1]
        elif headCoordinate[0] < tailCoordinate[0] and headCoordinate[1] < tailCoordinate[1]:
            return [tailCoordinate[0]-1, tailCoordinate[1]-1]

def partOneSolution():
    tailCoordinate = [0, 0]
    headCoordinate = [0, 0]
    visitedCoordinates = set()
    visitedCoordinates.add(tuple(tailCoordinate))
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip()
            input = line.split(' ')
            #print(input)
            for _ in range(int(input[1])):
                if input[0] == 'R':
                    headCoordinate[0] += 1
                elif input[0] == 'L':
                    headCoordinate[0] -= 1
                elif input[0] == 'U':
                    headCoordinate[1] += 1
                elif input[0] == 'D':
                    headCoordinate[1] -= 1
                
                if isHeadAdjacent(tailCoordinate, headCoordinate) == False:
                    tailCoordinate = newTailCoordinate(tailCoordinate, headCoordinate)
                    visitedCoordinates.add(tuple(tailCoordinate))
        # print(visitedCoordinates)
        return len(visitedCoordinates)


def partTwoSolution():
    knotCoordinates = {
        0: [0, 0],
        1: [0, 0],
        2: [0, 0],
        3: [0, 0],
        4: [0, 0],
        5: [0, 0],
        6: [0, 0],
        7: [0, 0],
        8: [0, 0],
        9: [0, 0],
    }
    visitedCoordinates = set()
    visitedCoordinates.add(tuple(knotCoordinates[9]))
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip()
            input = line.split(' ')
            #print(input)
            for _ in range(int(input[1])):
                if input[0] == 'R':
                    knotCoordinates[0][0] += 1
                elif input[0] == 'L':
                    knotCoordinates[0][0] -= 1
                elif input[0] == 'U':
                    knotCoordinates[0][1] += 1
                elif input[0] == 'D':
                    knotCoordinates[0][1] -= 1

                for i in range(1, 10):
                    previousKnot = i-1
                    currentKnot = i
                    if isHeadAdjacent(knotCoordinates[currentKnot],knotCoordinates[previousKnot]) == False:
                        knotCoordinates[currentKnot] = newTailCoordinate(knotCoordinates[currentKnot], knotCoordinates[previousKnot])
                        if currentKnot == 9:
                            visitedCoordinates.add(tuple(knotCoordinates[currentKnot]))
                    else:
                        break
                
        return len(visitedCoordinates)


def main():
    print(partOneSolution())
    print(partTwoSolution())
    

main()