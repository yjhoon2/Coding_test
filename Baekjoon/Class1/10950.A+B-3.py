import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(a+b)