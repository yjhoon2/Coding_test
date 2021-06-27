## 문자열 포매팅 방법 여러가지

# 내 풀이
def solution(seoul):
    idx = seoul.index("Kim")
    answer = f"김서방은 {idx}에 있다"
    return answer

# 다른사람 풀이
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))