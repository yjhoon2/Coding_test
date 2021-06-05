import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

a, b = map(int, input().split())

print(a+b)