import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

pin = list(map(int, input().split()))
answer = 0
for i in pin:
    answer += i**2

print(answer%10)