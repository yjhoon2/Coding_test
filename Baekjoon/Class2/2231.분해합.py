import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

m = int(input())
n = m - 9*len(str(m))
n = 1 if n < 1 else n

#1
while n < m:
    k = 0
    for i in range(len(str(n))):
        k += int(str(n)[i])
    if n + k == m:
        print(n)
        break
    else:
        n += 1
else:
    print(0)

#2
for x in range(n, m+1):
    sum_num = sum(list(map(int, str(x))))
    if x + sum_num == m:
        print(x)
        break
    if x == m:
        print(0)
