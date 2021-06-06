import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readlines

import sys
for line in sys.stdin:
    print(sum(map(int,line.split())))