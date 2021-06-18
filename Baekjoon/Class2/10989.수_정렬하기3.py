import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
'''
f = open(0) 
f.readline()
li=[0]*10001
for line in f:
    li[int(line)] += 1

for i in range(1, 10001):
    print(f'{i}\n' * li[i], end='')
'''
import sys

n = int(sys.stdin.readline())
res = [0] * 10001
for _ in range(n):
    a = int(sys.stdin.readline())
    res[a] += 1

for i in range(10001):
    if res[i] != 0:
        print(f'{i}\n' * res[i], end = '')

'''
import sys

n = int(sys.stdin.readline())
res = []
for _ in range(n):
    res.append(int(sys.stdin.readline()))
res.sort()
print('\n'.join(map(str, res)))
'''