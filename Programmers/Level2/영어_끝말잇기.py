def solution(n, words):
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0]:
            return [i%n+1, i//n+1]
        else:
            for j in range(i):
                if words[i] == words[j]:
                    return [i%n+1, i//n+1]
    else:
        return [0, 0]

# 같은 풀이지만 이게 더 간단하군
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]