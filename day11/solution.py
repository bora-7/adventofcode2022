# starting items: shows your worry level for each item
# operation: how your worry level changes as that monkey inspects an item
# before testing, divide new worry level by 3 (round down to nearest integer)
# test: how the monkey uses your new worry level to decide where to throw the item next

# first iterate through the entire array and store all monkeys in a dictionary
#

class Monkey:
    def __init__(self, items, operation, divideByTest, testTrue, testFalse):
        self.items = items
        self.operation = operation
        self.divideByTest = divideByTest
        self.testTrue = testTrue
        self.testFalse = testFalse


def partOneSolution():
    monkeyDictionary = {}
    monkeyNumberOfInspections = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
    }
    currentMonkeyInfo = []
    count = 0
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip()
            input = line.split(' ')
            if count == 0:
                currentMonkeyInfo.append(input[1])
            elif count == 1:
                
                integers = input[4:]
                for i in range(len(integers)-1):
                    integers[i] = integers[i].rstrip(integers[i][-1])

                for i in range(len(integers)):
                    integers[i] = int(integers[i])
                currentMonkeyInfo.append(integers)
            elif count == 2:
                currentMonkeyInfo.append(input[6:])
            elif count == 3:
                currentMonkeyInfo.append(input[5])
            elif count == 4:
                currentMonkeyInfo.append(input[9])
            elif count == 5:
                currentMonkeyInfo.append(input[9])
            else:
                count = -1
                #print(currentMonkeyInfo)
                tempMonkey = Monkey(currentMonkeyInfo[1], currentMonkeyInfo[2], currentMonkeyInfo[3], currentMonkeyInfo[4], currentMonkeyInfo[5])
                monkeyDictionary[int(currentMonkeyInfo[0][0])] = tempMonkey
                currentMonkeyInfo.clear()

            count += 1
            
    # for monkey in monkeyDictionary:
    #     print(monkey)
    #     print(monkeyDictionary[monkey].items)

    for _ in range(20):
        for monkeyNumber in monkeyDictionary:
            operation = monkeyDictionary[monkeyNumber].operation
            divideBy = int(monkeyDictionary[monkeyNumber].divideByTest)
            testTrue = int(monkeyDictionary[monkeyNumber].testTrue)
            testFalse = int(monkeyDictionary[monkeyNumber].testFalse)

            for item in monkeyDictionary[monkeyNumber].items:
                item = int(item)
                monkeyNumberOfInspections[monkeyNumber] += 1
                # possible operations are just add and multiply
                if operation[0] == '*':
                    if operation[1] == 'old':
                        item = item * item
                    else:
                        item = item * int(operation[1])
                else:
                    item = item + int(operation[1])

                item = item // 3

                if item % divideBy == 0:
                    monkeyDictionary[testTrue].items.append(item)
                else:
                    monkeyDictionary[testFalse].items.append(item)
            
            monkeyDictionary[monkeyNumber].items = []
    
    monkeyValues = list(monkeyNumberOfInspections.values())
    monkeyValues.sort()
    return monkeyValues[-1] * monkeyValues[-2]


# ---------------------------------------------------------
def partTwoSolution():
    monkeyDictionary = {}
    monkeyNumberOfInspections = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
    }
    currentMonkeyInfo = []
    count = 0
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip()
            input = line.split(' ')
            if count == 0:
                currentMonkeyInfo.append(input[1])
            elif count == 1:
                
                integers = input[4:]
                for i in range(len(integers)-1):
                    integers[i] = integers[i].rstrip(integers[i][-1])

                for i in range(len(integers)):
                    integers[i] = int(integers[i])
                currentMonkeyInfo.append(integers)
            elif count == 2:
                currentMonkeyInfo.append(input[6:])
            elif count == 3:
                currentMonkeyInfo.append(input[5])
            elif count == 4:
                currentMonkeyInfo.append(input[9])
            elif count == 5:
                currentMonkeyInfo.append(input[9])
            else:
                count = -1
                #print(currentMonkeyInfo)
                tempMonkey = Monkey(currentMonkeyInfo[1], currentMonkeyInfo[2], currentMonkeyInfo[3], currentMonkeyInfo[4], currentMonkeyInfo[5])
                monkeyDictionary[int(currentMonkeyInfo[0][0])] = tempMonkey
                currentMonkeyInfo.clear()

            count += 1
            
    # for monkey in monkeyDictionary:
    #     print(monkey)
    #     print(monkeyDictionary[monkey].items)
    modulo = 1
    for monkey in monkeyDictionary:
        modulo *= int(monkeyDictionary[monkey].divideByTest)
    for _ in range(10000):
        for monkeyNumber in monkeyDictionary:
            operation = monkeyDictionary[monkeyNumber].operation
            divideBy = int(monkeyDictionary[monkeyNumber].divideByTest)
            testTrue = int(monkeyDictionary[monkeyNumber].testTrue)
            testFalse = int(monkeyDictionary[monkeyNumber].testFalse)

            for item in monkeyDictionary[monkeyNumber].items:
                item = int(item)
                monkeyNumberOfInspections[monkeyNumber] += 1
                # possible operations are just add and multiply
                if operation[0] == '*':
                    if operation[1] == 'old':
                        item = item * item
                    else:
                        item = item * int(operation[1])
                else:
                    item = item + int(operation[1])

                item = item % modulo

                if item % divideBy == 0:
                    monkeyDictionary[testTrue].items.append(item)
                else:
                    monkeyDictionary[testFalse].items.append(item)
            
            monkeyDictionary[monkeyNumber].items = []
    
    monkeyValues = list(monkeyNumberOfInspections.values())
    monkeyValues.sort()
    return monkeyValues[-1] * monkeyValues[-2]

def main():
    print(partOneSolution())
    print(partTwoSolution())
    

main()