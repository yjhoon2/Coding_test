import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
print(min(num), max(num))