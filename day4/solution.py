
def partOneSolution():
    count = 0
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip()
            input = line.split(',')
            # print(input)
            firstRange = input[0].split('-')
            # print(firstRange)
            secondRange = input[1].split('-')
            # print(secondRange)
            
            if (int(firstRange[0]) <= int(secondRange[0]) and int(firstRange[1]) >= int(secondRange[1])) or (int(secondRange[0]) <= int(firstRange[0]) and int(secondRange[1]) >= int(firstRange[1])):
                count += 1
    
    return count



def partTwoSolution():
    count = 0
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip()
            input = line.split(',')
            # print(input)
            firstRange = input[0].split('-')
            # print(firstRange)
            secondRange = input[1].split('-')
            # print(secondRange)
            
            # if (int(firstRange[0]) <= int(secondRange[0]) and int(firstRange[1]) >= int(secondRange[1])) or (int(secondRange[0]) <= int(firstRange[0]) and int(secondRange[1]) >= int(firstRange[1])):
            #     count += 1
            if (int(firstRange[0]) >= int(secondRange[0]) and int(firstRange[0]) <= int(secondRange[1])) or (int(secondRange[0]) >= int(firstRange[0]) and int(secondRange[0]) <= int(firstRange[1])):
                count += 1
            
    return count



def main():
    print(partOneSolution())
    print(partTwoSolution())
    

main()