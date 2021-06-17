import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    age, name = input().split()
    age = int(age)
    arr.append((age, name, i))
#print(arr)
arr.sort(key = lambda x : (x[0], x[2]))
#print(arr)
for i in range(n):
    print(arr[i][0], arr[i][1])