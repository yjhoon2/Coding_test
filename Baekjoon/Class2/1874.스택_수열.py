### 내 풀이
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
nums = [x for x in range(1, n+1)]
arr = []
for _ in range(n):
    arr.append(int(input()))

result = []
answer = []
stack = []

for i in range(n):
    if len(nums) == 0:
        while stack:
            b = stack.pop()
            result.append(b)
            answer.append('-')
    if len(stack) != 0 and stack[-1] == arr[i]:
        b = stack.pop()
        result.append(b)
        answer.append('-')
        continue
    while nums:
        a = nums.pop(0)
        stack.append(a)
        answer.append('+')
        if stack[-1] == arr[i]:
            b = stack.pop()
            result.append(b)
            answer.append('-')
            break
else:
    if result == arr:
        for k in answer:
            print(k)
    else:
        print("NO")


### 이게 찐이다...
import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
p = []
for _ in range(n):
    p.append(int(input()))
print(p)
def solution():
    stack, result, cnt = [], [], 1
    for i in p:
        while cnt <= i:
            stack.append(cnt)
            result.append('+')
            cnt += 1
        if stack.pop() != i:
            return 'NO'
        else:
            result.append('-')
    return '\n'.join(result)

print(solution())
