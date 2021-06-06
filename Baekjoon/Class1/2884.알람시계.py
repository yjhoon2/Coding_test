import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

h, m = map(int, input().split())

if m < 45:
    mm = 60 - abs(m-45)
    if h == 0:
        hh = 23
    else:
        hh = h -1
else:
    hh = h
    mm = m - 45
print(hh, mm)