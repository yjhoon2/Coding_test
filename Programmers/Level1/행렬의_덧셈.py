def solution(arr1, arr2):
    return [[i+j for i, j in zip(arr1[k], arr2[k])] for k in range(len(arr1))]