
def partOneSolution():
    windowStart = 0
    charFrequency = {}
    result = 0
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip()
            for windowEnd in range(14):
                if line[windowEnd] not in charFrequency:
                    charFrequency[line[windowEnd]] = 0
                charFrequency[line[windowEnd]] += 1
                
                if len(charFrequency) == 14:
                    result = windowEnd + 1
                    return result
            for windowEnd in range(14, len(line)):
                elementToRemove = line[windowStart]
                windowStart += 1
                charFrequency[elementToRemove] -= 1
                if charFrequency[elementToRemove] == 0:
                    del charFrequency[elementToRemove]
                
                if line[windowEnd] not in charFrequency:
                    charFrequency[line[windowEnd]] = 0
                charFrequency[line[windowEnd]] += 1

                if len(charFrequency) == 14:
                    result = windowEnd + 1
                    return result

            




def partTwoSolution():
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip()
            input = line.split(',')




def main():
    print(partOneSolution())
    #print(partTwoSolution())
    

main()