def solution(n):
    cnt = 0
    for i in range(1, n//2+1):
        sum = 0
        for x in range(i, n):
            sum += x
            if sum == n:
                cnt += 1
                break
            elif sum > n:
                break
    return cnt+1

# 내 풀이를 좀 더 간단하게
def expressions(num):
    answer = 0
    for i in range(1, num + 1):
        s = 0
        while s < num:
            s += i
            i += 1
        if s == num:
            answer += 1
    return answer

## 일정한 규칙이 있었음
# n의 약수 중 홀수가 몇개있냐는 문제
# 이해 안됨
def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])