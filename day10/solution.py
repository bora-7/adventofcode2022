# signal strength: cycle number x value of X
# calculate it DURING 20th cycle -> DURING 60th cycle -> DURING 100th cycle and so on
# (cycleCount - 20) % 40 == 0
def partOneSolution():
    cycleCount = 1
    x = 1
    totalSum = 0
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip()
            input = line.split(' ')
            if (cycleCount - 20) % 40 == 0:
                totalSum += (x * cycleCount)

            if input[0] == 'noop':
                cycleCount += 1
            else:
                cycleCount += 1
                if (cycleCount - 20) % 40 == 0:
                    totalSum += (x * cycleCount)
                cycleCount += 1
                x += int(input[1])

            if cycleCount > 220:
                break
        
    return totalSum


# first calculate sprite position, see if it overlaps with the current sprite being drawn
def partTwoSolution():
    pixels = [[-1 for i in range(40)] for i in range(6)]
    cycleCount = 1
    x = 1
    rowNumber = -1
    with open('input.txt') as f:
        for line in f:
            #print(x)
            line = line.rstrip()
            input = line.split(' ')
            
            if (cycleCount - 1) % 40 == 0:
                rowNumber += 1

            if x == ((cycleCount - 1) % 40) or x-1 == (cycleCount - 1) % 40 or x+1 == (cycleCount - 1) % 40:
                pixels[rowNumber][(cycleCount - 1) % 40] = '.'
            else:
                pixels[rowNumber][(cycleCount - 1) % 40] = '#'
            if input[0] == 'noop':
                cycleCount += 1
            else:
                cycleCount += 1
                if (cycleCount - 1) % 40 == 0:
                    rowNumber += 1
                if x == ((cycleCount - 1) % 40) or x-1 == (cycleCount - 1) % 40 or x+1 == (cycleCount - 1) % 40:
                    pixels[rowNumber][(cycleCount - 1) % 40] = '.'
                else:
                    pixels[rowNumber][(cycleCount - 1) % 40] = '#'

                    
                cycleCount += 1

                x += int(input[1])

    return pixels




def main():
    print(partOneSolution())
    print(partTwoSolution())
    

main()