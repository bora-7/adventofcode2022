from collections import deque
from collections import defaultdict
import heapq
import string

# start from S, get to E with fewest steps possible
# elevation of the square your travellingcan be at most one higher

# see it as a graph problem use BFS to get shortest path
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
def partOneSolution():
    with open('input.txt') as f:
        input = f.read().strip().split()
    
    heights = [list(x) for x in input]
    #print(input)
    rowsLength = len(heights)
    colLength = len(heights[0])
    sx, sy = [(i,j) for i in range(rowsLength) for j in range(colLength) if heights[i][j] == "S"][0]
    tx, ty = [(i,j) for i in range(rowsLength) for j in range(colLength) if heights[i][j] == "E"][0]


    heights[sx][sy] = 'a'
    heights[tx][ty] = 'z'

    def height(s):
        return string.ascii_lowercase.index(s)
    
    def neighbours(i, j):
        result = []
        for di, dj in dirs:
            newI = i + di
            newJ = j + dj
            
            if not (newI >= 0 and newJ >= 0 and newI < rowsLength and newJ < colLength):
                continue
            
            if height(heights[newI][newJ]) - 1 <= height(heights[i][j]):
                result.append((newI, newJ))
            
        return result

    # implement djisktra's
    visited = [[False] * colLength for _ in range(rowsLength)]
    heap = [(0, sx, sy)]

    while True:
        #print(len(heap))
        steps, i, j = heapq.heappop(heap)

        if visited[i][j]:
            continue
        visited[i][j] = True

        if i == tx and j == ty:
            return steps
        
        for ii, jj in neighbours(i, j):
            heapq.heappush(heap, (steps+1, ii, jj))

def partTwoSolution():
    # start at E and end at any 'a' location

    with open('input.txt') as f:
        input = f.read().strip().split()
    
    heights = [list(x) for x in input]
    #print(input)
    rowsLength = len(heights)
    colLength = len(heights[0])
    sx, sy = [(i,j) for i in range(rowsLength) for j in range(colLength) if heights[i][j] == "S"][0]
    tx, ty = [(i,j) for i in range(rowsLength) for j in range(colLength) if heights[i][j] == "E"][0]


    heights[sx][sy] = 'a'
    heights[tx][ty] = 'z'
    newStartX = tx
    newStartY = ty

    def height(s):
        return string.ascii_lowercase.index(s)
    
    def neighbours(i, j):
        result = []
        for di, dj in dirs:
            newI = i+di
            newJ = j + dj
            
            if not (newI >= 0 and newJ >= 0 and newI < rowsLength and newJ < colLength):
                continue
            
            if height(heights[newI][newJ]) + 1 >= height(heights[i][j]):
                result.append((newI, newJ))
            
        return result

    # implement djisktra's
    visited = [[False] * colLength for _ in range(rowsLength)]
    heap = [(0, newStartX, newStartY)]

    while True:
        steps, i, j = heapq.heappop(heap)

        if visited[i][j]:
            continue
        visited[i][j] = True

        if heights[i][j] == 'a':
            return steps
    
        for ii, jj in neighbours(i, j):
            heapq.heappush(heap, (steps+1, ii, jj))

def main():
    print(partOneSolution())
    print(partTwoSolution())

main()