import heapq

def mostCaloriesForAllElves():
    biggestSoFar = 0
    current = 0

    with open('input.txt') as f:
        for line in f:
            if line.rstrip() == '':
                current = 0
            else:
                current += int(line.rstrip())
                biggestSoFar = max(biggestSoFar, current)

    return biggestSoFar

def topThreeSum():
    minHeap = [] # will always store 3 elements
    current = 0
    # populate minHeap with the first 3 sums first:
    counter = 0
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip()
            if counter == 0:
                heapq.heappush(minHeap, current)
                counter += 1
                continue
            if line == '':
                if minHeap[0] < current:
                    heapq.heappush(minHeap, current)
                    if len(minHeap) > 3:
                        heapq.heappop(minHeap)
                current = 0
            else:
                current += int(line)
    
    result = 0
    for num in minHeap:
        result += num
    
    return result

def main():
    print(mostCaloriesForAllElves())
    print(topThreeSum())

main()
