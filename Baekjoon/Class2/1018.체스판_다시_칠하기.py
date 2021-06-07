import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n, m = map(int, input().split())
mat = [list(input().rstrip()) for _ in range(n)]

