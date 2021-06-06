import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())

for i in range(1, 10):
    print(f"{n} * {i} = {n*i}")