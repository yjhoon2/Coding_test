import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

# 내 풀이
from sys import stdin

n = int(stdin.readline())
stack = []

for _ in range(n):
    inp = stdin.readline().split()
    if len(inp) == 2:
        stack.append(int(inp[1]))
    else:
        if inp[0] == 'pop':
            if len(stack) != 0:
                print(stack.pop())
            else:
                print(-1)
        elif inp[0] == 'size':
            if len(stack) != 0:
                print(len(stack))
            else:
                print(0)
        elif inp[0] == 'empty':
            if len(stack) != 0:
                print(0)
            else:
                print(1)
        elif inp[0] == 'top':
            if len(stack) != 0:
                print(stack[-1])
            else:
                print(-1)


# 다른사람 풀이 (시간 단축하는거 위주로 보자)
from sys import stdin

stack = []
next(stdin)
for line in stdin:
    command = line.split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if stack: print(stack.pop())
        else: print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if stack: print(0)
        else: print(1)
    elif command[0] == 'top':
        if stack: print(stack[-1])
        else: print(-1)