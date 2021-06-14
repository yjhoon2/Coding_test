import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n, m = map(int, input().split())

x = max(n, m)
y = min(n, m)

# 유클리드 호제법
while x % y != 0:
    x, y = y, x%y
print(y) 

print(n*m//y)