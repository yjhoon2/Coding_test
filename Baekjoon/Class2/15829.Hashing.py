import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

import sys
n = int(sys.stdin.readline())
word = sys.stdin.readline()
res = 0
for i in range(n):
    res += (ord(word[i])-96)*(31**i)    
print(res)