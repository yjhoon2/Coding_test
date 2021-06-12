## 내 풀이
def solution(s):
    arr = []
    for x in s:
        arr.append(ord(x))
    arr.sort(reverse = True)
    answer = ''
    for k in arr:
        answer += chr(k)
    return answer

## 다른사람 풀이
# 난 sort만 해봤는데 안되길래 아스키로 했는데 sorted는 되네...
def solution(s):
    s = sorted(s, reverse = True)
    #s.sort()
    return ''.join(s)