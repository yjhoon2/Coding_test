import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline


# 풀이1
n = int(input())
print(sum(map(int, input())))

# 풀이2
n = int(input())
num = input()
answer = 0
for i in range(n):
    answer += int(num[i])
print(answer)