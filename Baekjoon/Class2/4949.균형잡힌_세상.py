import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

while True:
    a = input()
    if a[0] == ".":
        break
    else:
        stack = []
        for x in a:
            if x == "[" or x == "(":
                stack.append(x)
            elif x == "]":
                if len(stack) != 0 and stack[-1] == "[":
                    stack.pop() 
                else:
                    stack.append(x)
                    break
            elif x == ")":
                if len(stack) != 0 and stack[-1] == "(":
                    stack.pop() 
                else:
                    stack.append(x)
                    break
        if len(stack) == 0:
            print("yes")
        else:
            print("no")