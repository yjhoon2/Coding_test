import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

rest = []
for i in range(10):
    rest.append(int(input())%42)
print(len(set(rest)))