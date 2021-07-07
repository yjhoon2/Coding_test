def solution(clothes):
    dict = {}
    for c in clothes:
        dict[c[1]] = dict.get(c[1], 0) + 1
    if len(dict) == 1:
        return sum(dict.values())
    else:
        ans = 1
        for x in dict.values():
            ans *= (x+1) # 안 입었을 경우까지 포함해서 +1
        return ans - 1 # 전부 안 입었을 경우 제거 -1