import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())

arr = [-1] * (n+1)
if n >= 3 and n < 5:
    arr[3] = 1
elif n >= 5:
    arr[3], arr[5] = 1, 1
for i in range(6, n+1):
    if arr[i-3] == -1 and arr[i-5] == -1:
        arr[i] = -1
    elif arr[i-3] != -1 and arr[i-5] != -1:
        arr[i] = min(arr[i-3], arr[i-5]) + 1
    elif arr[i-3] == -1:
        arr[i] = arr[i-5] + 1
    else:
        arr[i] = arr[i-3] + 1
print(arr[n])


# 다른 풀이1
n = int(input())

a = n//5
b = n%5
c = 0

while a>=0:
    if b%3 == 0:
        c = b//3
        
        break
    a -= 1
    b += 5
        
if b%3 == 0:
    print(a+c)
else:
    print(-1)

# 다른 풀이2
N = int(input())
cnt = 0
while True:
    if (N % 5) == 0:
        cnt = cnt + (N // 5)
        print(cnt)
        break
    N -= 3
    cnt += 1
    if N < 0:
        print(-1)
        break