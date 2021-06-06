import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

for i in range(int(input()), 0, -1):
    print(i)