import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()

def binary_research(l, arr):
    lt = 0
    rt = n-1
    while lt <= rt:
        mid = (lt+rt)//2
        if l == arr[mid]:
            return print(1)
        elif l < arr[mid]:
            rt = mid-1
        else:
            lt = mid+1
    return print(0)

for x in arr2:
    binary_research(x, arr1)