import string

lowercaseAlphabet = list(string.ascii_lowercase)
uppercaseAlphabet = list(string.ascii_uppercase)

counter = 1
priorities = {}
for char in lowercaseAlphabet:
    priorities[char] = counter
    counter += 1


for char in uppercaseAlphabet:
    priorities[char] = counter
    counter += 1



def  partOneSolution():
    totalPriority = 0
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip()
            halfWayPoint = len(line) // 2

            mySet = set()
            for i in range(halfWayPoint):
                if line[i] not in mySet:
                    mySet.add(line[i])
            
            for i in range(halfWayPoint, len(line)):
                if line[i] in mySet:
                    totalPriority += priorities[line[i]]
                    break
            
    return totalPriority


def partTwoSolution():
    totalPriority = 0
    counter = 0
    mySet1 = set()
    mySet2 = set()
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip()
            if counter == 0:
                for i in range(len(line)):
                    if line[i] not in mySet1:
                        mySet1.add(line[i])
            if counter == 1:
                for i in range(len(line)):
                    if line[i] in mySet1:
                        mySet2.add(line[i])
            if counter == 2:
                for i in range(len(line)):
                    if line[i] in mySet2:
                        totalPriority += priorities[line[i]]
                        mySet1.clear()
                        mySet2.clear()
                        counter = -1
                        break
            counter += 1
        
    return totalPriority


def main():
    print(partOneSolution())
    print(partTwoSolution())
    

main()