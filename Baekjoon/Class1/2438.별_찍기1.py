import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
for i in range(1, n+1):
    print("*"*i)