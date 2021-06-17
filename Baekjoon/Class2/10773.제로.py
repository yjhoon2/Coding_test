import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

'''
n = int(input())
stack = []
for _ in range(n):
    a = int(input())
    if a == 0:
        stack.pop()
    else:
        stack.append(a)
print(sum(stack))
'''

# 이게 시간 40배는 단축해줌
from sys import stdin

input()
stack = []
#print(list(map(int, stdin)))

for x in map(int, stdin):
    if x:
        stack.append(x)
    else:
        stack.pop()

print(sum(stack))