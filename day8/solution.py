from collections import defaultdict


def partOneSolution():
    map = []
    result = 0
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip()
            input = list(line)
            #print(input)
            map.append(input)
    numberOfColumns = len(map[0])
    numberOfRows = len(map)

    result += (2*numberOfColumns + 2*numberOfRows) - 4

    for i in range(1, numberOfRows-1):
        for j in range(1, numberOfColumns-1):
            if helper1(map, i, j) == True:
                result += 1
            
    return result
    

def helper1(map, i, j):
    number = map[i][j]
    notVisible = 0
    
    # first go left:
    temp = j-1
    while (temp >= 0):
        if map[i][temp] >= number:
            notVisible += 1
            break
        temp -= 1
        
    # go right
    temp = j+1
    while (temp < len(map[0])):
        if map[i][temp] >= number:
            notVisible += 1
            break
        temp += 1
        
    # go up
    temp = i-1
    while (temp >= 0):
        if map[temp][j] >= number:
            notVisible += 1
            break
        temp -= 1

    # go down
    temp = i+1
    while (temp < len(map)):
        if map[temp][j] >= number:
            notVisible += 1
            break
        temp += 1

    if notVisible < 4:
        return True
    else:
        return False

def partTwoSolution():
    map = []
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip()
            input = list(line)
            map.append(input)

    numberOfColumns = len(map[0])
    numberOfRows = len(map)


    maxVisible = 0
    for i in range(1, numberOfRows-1):
        for j in range(1, numberOfColumns-1):
            maxVisible = max(maxVisible, helper2(map, i, j))
            
    return maxVisible

def helper2(map, i, j):
    number = map[i][j]
    
    # first go left:
    temp = j-1
    visibleFromLeft = 0
    while (temp >= 0):
        if map[i][temp] >= number:
            visibleFromLeft += 1
            break
        temp -= 1
        visibleFromLeft += 1
        
    # go right
    temp = j+1
    visibleFromRight = 0
    while (temp < len(map[0])):
        if map[i][temp] >= number:
            visibleFromRight += 1
            break
        temp += 1
        visibleFromRight += 1
        
    # go up
    temp = i-1
    visibleFromUp = 0
    while (temp >= 0):
        if map[temp][j] >= number:
            visibleFromUp += 1
            break
        temp -= 1
        visibleFromUp += 1

    # go down
    temp = i+1
    visibleFromDown = 0
    while (temp < len(map)):
        if map[temp][j] >= number:
            visibleFromDown += 1
            break
        temp += 1
        visibleFromDown += 1

    result = visibleFromDown * visibleFromLeft * visibleFromRight * visibleFromUp
    return result

def main():
    print(partOneSolution())
    print(partTwoSolution())
    

main()