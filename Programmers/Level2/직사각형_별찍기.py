## 내 풀이
a, b = map(int, input().strip().split(' '))
for _ in range(b):
    print("*"*a)

## 다른사람 풀이
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)