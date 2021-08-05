# 아니 개어렵네 ㅁㅊ...

def DFS(begin, target, words, visit):
    answer = 0
    stack = [begin]
    while stack:
        w = stack.pop()
        if w == target:
            return answer
        
        for i in range(len(words)):
            diff = 0
            if visit[i] == 0:
                for a, b in zip(w, words[i]):
                    if a != b:
                        diff += 1
                if diff == 1:
                    stack.append(words[i])
                    visit[i] = 1
        answer += 1
    return answer
        

def solution(begin, target, words):
    visit = [0] * len(words)
    if target not in words:
        return 0
    
    return DFS(begin, target, words, visit)