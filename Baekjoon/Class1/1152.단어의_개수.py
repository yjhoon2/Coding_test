import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

a = list(input().split())
print(len(a))