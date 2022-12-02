# A = X = Rock = 1 point
# B = Y = Paper = 2 points
# C = Z = Scissors = 3 points

# +3 if you draw, +6 if you win


shapeScore = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3,
}

outcomeTable = {
    ('A', 'X') : [3, 'Z'],
    ('A', 'Y') : [6, 'X'],
    ('A', 'Z') : [0, 'Y'],
    ('B', 'X') : [0, 'X'],
    ('B', 'Y') : [3, 'Y'],
    ('B', 'Z') : [6, 'Z'],
    ('C', 'X') : [6, 'Y'],
    ('C', 'Y') : [0, 'Z'],
    ('C', 'Z') : [3, 'X']
}

def calculateStrategyScore():
    totalScore = 0
    with open('input.txt') as f:
        for line in f:
            currentScore = 0
            line = line.rstrip()
            input = line.split(' ')
            inputTuple = (input[0], input[1])
            if input != None:
                currentScore = shapeScore[input[1]] + outcomeTable[inputTuple][0]
                totalScore += currentScore

    return totalScore

def calculateTrueStrategyScore():
    totalScore = 0
    with open('input.txt') as f:
        for line in f:
            currentScore = 0
            line = line.rstrip()
            input = line.split(' ')
            inputTuple = (input[0], input[1])
            if input != None:
                # first find out what to play
                needToPlay = outcomeTable[inputTuple][1]
                newTuple = (input[0], needToPlay)
                currentScore = shapeScore[needToPlay] + outcomeTable[newTuple][0]
                totalScore += currentScore

    return totalScore

def main():
    print(calculateStrategyScore())
    print(calculateTrueStrategyScore())

main()