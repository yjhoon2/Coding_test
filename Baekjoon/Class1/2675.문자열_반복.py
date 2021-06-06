import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

T = int(input())
for i in range(T):
    P, S = input().split()
    for j in S:
        print(j * int(P), end = '')
    print()