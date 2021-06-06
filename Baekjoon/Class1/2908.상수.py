import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

a, b = input().split()
print(max(int(a[::-1]), int(b[::-1])))