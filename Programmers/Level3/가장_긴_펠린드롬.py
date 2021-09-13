def solution(s):
    answer = 0
    for n in range(len(s), 0, -1):
        for start in range(0, len(s)):
            if n + start > len(s):
                break
            word = s[start:start+n]
            
            if word == word[::-1]:
                answer = len(word)
                return answer
