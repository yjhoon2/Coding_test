import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

import sys
for line in sys.stdin:
    a, b = map(int, line.split())
    if a ==0 and b == 0:
        break
    else:
        print(a+b)