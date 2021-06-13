import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
st = 1
cnt = 0
while st + 6*cnt < n:
    st += 6*cnt
    cnt += 1
print(cnt + 1)
