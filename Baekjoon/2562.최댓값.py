import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

num = []
for _ in range(9):
    num.append(int(input()))
print(max(num))
print(num.index(max(num))+1)

