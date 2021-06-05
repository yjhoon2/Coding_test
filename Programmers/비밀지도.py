# 내 풀이
def two(k, n):
    tmp = ''
    for i in range(n-1, -1, -1):
        tmp += str(k // (2**i))
        k -= (2**i)*(k // (2**i))
    return tmp
            
answer = []
def solution(n, arr1, arr2):
    for i in range(n):
        inp = ''
        a = two(arr1[i], n)
        b = two(arr2[i], n)
        for j in range(n):
            if a[j] == '1' or b[j] == '1':
                inp += '#'
            else:
                inp += ' '
        answer.append(inp)
    
    return answer




# 다른사람 풀이 1
# 비트연산자 사용

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer



# 다른사람 풀이 2
# 정규표현식 사용

import re

def solution(n, arr1, arr2):
    answer = ["#"]*n
    for i in range(0, n):
        answer[i] = str(bin(arr1[i]|arr2[i]))[2:]
        answer[i] = re.sub('1', '#', '0'*(n-len(answer[i]))+answer[i])
        answer[i] = re.sub('0', ' ', answer[i])
    return answer