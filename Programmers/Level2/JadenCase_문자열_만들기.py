# 질문하기 보니까 공백이 여러개 나오는 경우가 있어서 split함수 안될 듯...
def solution(s):
    s=s.lower()
    arr = s.split()
    for i in range(len(arr)):
        arr[i][0] = arr[i][0].upper()
    
    return ' '.join(arr)
print(solution("3people unFollowed me"))

# 이제 됨
def solution(s):
    s=s.lower()
    answer = s[0].upper()
    for i in range(1, len(s)):
        if s[i-1] == ' ':
            answer += s[i].upper()
        else:
            answer += s[i]
    return answer