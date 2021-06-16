import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    vps = input()
    stack = []
    for x in vps:
        if x == '(':
            stack.append(x)
        elif x == ')':
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(x)
                break
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")