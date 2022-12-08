from collections import defaultdict


def partOneSolution():
    directoryStack = []
    directorySums = defaultdict(int)
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip()
            input = line.split(' ')
            #print(input)
            if input[1] == 'cd':
                if input[2] == '..':
                    directoryStack.pop()
                else:
                    directoryStack.append(input[2])

            elif input[0] != '$' and input[0] != 'dir':
                for i in range(len(directoryStack)):
                    directorySums[tuple(directoryStack[:i+1])] += int(input[0])

            
    print(directorySums)
    return sum(size for size in directorySums.values() if size<=100000)

def partTwoSolution():
    directoryStack = []
    directorySums = defaultdict(int)
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip()
            input = line.split(' ')
            #print(input)
            if input[1] == 'cd':
                if input[2] == '..':
                    directoryStack.pop()
                else:
                    directoryStack.append(input[2])

            elif input[0] != '$' and input[0] != 'dir':
                print('START')
                for i in range(len(directoryStack)):
                    print(tuple(directoryStack[:i+1]))
                    directorySums[tuple(directoryStack[:i+1])] += int(input[0])
                print('END')

            
    required = 30000000 - (70000000 - directorySums[('/',)])
    return min(size for size in directorySums.values() if size >= required)

def main():
    #print(partOneSolution())
    print(partTwoSolution())
    

main()