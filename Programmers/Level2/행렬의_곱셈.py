def solution(arr1, arr2):
    n = len(arr1)
    m = len(arr2[0])
    arr = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(len(arr1[0])):
                arr[i][j] += arr1[i][k] * arr2[k][j]
        
    return arr

# 나도 zip으로 풀고 싶었는데...
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]