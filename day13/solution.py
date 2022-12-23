from collections import deque
from collections import defaultdict
import ast
import heapq
import string
from functools import cmp_to_key

# first parse the input file and get a list of pairs
def partOneSolution():
    result = 0
    pairs = []
    temp = []
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip()
            #print(line)
            if line == '':
                pairs.append(temp)
                #print(temp)
                temp = []
            else:
                temp.append(line)

    def compare(a, b):
        if isinstance(a, int) and isinstance(b, int):
            if a < b:
                return 1
            elif a == b:
                return 0
            else:
                return -1
        
        if isinstance(a, int) and isinstance(b, list):
            a = [a]
        elif isinstance(a, list) and isinstance(b, int):
            b = [b]
        
        if isinstance(a, list) and isinstance(b, list):
            i = 0
            while i < len(a) and i < len(b):
                result = compare(a[i], b[i])
                if result == 1:
                    return 1
                elif result == -1:
                    return -1
                i += 1
            
            if i == len(a):
                if i == len(b):
                    return 0
                else:
                    return 1
            
            return -1

    for i in range(len(pairs)):
        elem1 = ast.literal_eval(pairs[i][0])
        elem2 = ast.literal_eval(pairs[i][1])
        
        if compare(elem1, elem2) == 1:
            result += i + 1

    return result

def partTwoSolution():
    result = 1
    input = []
    
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip()
            #line = ast.literal_eval(line)
            #print(line)
            if line == '':
                continue
            else:
                input.append(line)

    input = list(map(eval, input))
    input.append([[2]])
    input.append([[6]])

    def compare(a, b):

        if isinstance(a, int) and isinstance(b, int):
            if a < b:
                return 1
            elif a == b:
                return 0
            else:
                return -1
        
        if isinstance(a, int) and isinstance(b, list):
            a = [a]
        elif isinstance(a, list) and isinstance(b, int):
            b = [b]
        
        if isinstance(a, list) and isinstance(b, list):
            i = 0
            while i < len(a) and i < len(b):
                result = compare(a[i], b[i])
                if result == 1:
                    return 1
                elif result == -1:
                    return -1
                i += 1
            
            if i == len(a):
                if i == len(b):
                    return 0
                else:
                    return 1
            
            return -1

    input = sorted(input, key=cmp_to_key(compare), reverse=True)

    for i in range(len(input)):
        if input[i] == [[2]]:
            a = i+1
        elif input[i] == [[6]]:
            b = i+1
    
    result = a * b
    return result

def main():
    print(partOneSolution())
    print(partTwoSolution())

main()