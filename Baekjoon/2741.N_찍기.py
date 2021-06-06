import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

for i in range(1, int(input())+1):
    print(i)