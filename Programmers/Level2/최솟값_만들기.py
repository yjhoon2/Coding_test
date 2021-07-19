def solution(A,B):
    A.sort()
    B.sort(reverse = True)
    answer = 0
    for i in range(len(A)):
        answer += A[i]*B[i]
    return answer

# zip 함수 사용하자..
def getMinSum(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))