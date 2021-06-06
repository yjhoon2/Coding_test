import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline


num = 1
for _ in range(3):
    num = num * int(input())

for i in range(10):
    print(str(num).count(str(i)))

# 이렇게도 품
d=input
a=int(d())*int(d())*int(d())
for j in range(10):
    print(str(a).count(str(j)))