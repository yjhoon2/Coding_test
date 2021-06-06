import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
score = list(map(int, input().split()))

print((sum(score)/n)*100/max(score))