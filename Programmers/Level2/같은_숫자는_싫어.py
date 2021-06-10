# 내 풀이
def solution(arr):
    num = arr[0]
    answer = [num]
    for i in range(len(arr)):
        if arr[i] != num:
            num = arr[i]
            answer.append(num)
    return answer

# 다른사람 풀이
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue # a 리스트에 마지막 수가 i와 같으면 밑에 코드 생략하고 건너뜀.
        a.append(i)
    return a