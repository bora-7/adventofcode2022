stack1 = ['D', 'H', 'N', 'Q', 'T', 'W', 'V', 'B']
stack2 = ['D', 'W', 'B']
stack3 = ['T', 'S', 'Q', 'W', 'J', 'C']
stack4 = ['F', 'J', 'R', 'N', 'Z', 'T', 'P']
stack5 = ['G', 'P', 'V', 'J', 'M', 'S', 'T']
stack6 = ['B', 'W', 'F', 'T', 'N']
stack7 = ['B', 'L', 'D', 'Q', 'F', 'H', 'V', 'N']
stack8 = ['H', 'P', 'F', 'R']
stack9 = ['Z', 'S', 'M', 'B', 'L', 'N', 'P', 'H']

myDictionary = {
    1:stack1,
    2:stack2,
    3:stack3,
    4:stack4,
    5:stack5,
    6:stack6,
    7:stack7,
    8:stack8,
    9:stack9
}

def partOneSolution():
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip()
            input = line.split(' ')
            numberOfCrates = int(input[1])
            moveFrom = int(input[3])
            moveTo = int(input[5])

            for _ in range(numberOfCrates):
                temp = myDictionary[moveFrom].pop()
                myDictionary[moveTo].append(temp)
    result = ""
    for i in range(1, 10):
        result += myDictionary[i][-1]
    
    return result



def partTwoSolution():
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip()
            input = line.split(' ')
            numberOfCrates = int(input[1])
            moveFrom = int(input[3])
            moveTo = int(input[5])
            
            temp = []
            for _ in range(numberOfCrates):
                if len(myDictionary[moveFrom]) == 0:
                    break
                temp.append(myDictionary[moveFrom].pop())
            

            temp.reverse()
            myDictionary[moveTo].extend(temp)
    result = ""
    for i in range(1, 10):
        result += myDictionary[i][-1]
    
    return result


def main():
    print(partOneSolution())
    print(partTwoSolution())
    

main()