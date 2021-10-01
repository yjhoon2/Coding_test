# 이렇게 하려고 했는데 홀수가 너무 복잡하네..

def solution(sticker):
    answer = 0
    if len(sticker)%2 == 0:
        a, b = 0, 0
        for i in range(len(sticker)):
            if i%2 == 0:
                a += sticker[i]
            else:
                b += sticker[i]
        answer = max(a, b)
        

    return answer

    
# DP 사용
def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    answer = 0
    table1 = [0] * len(sticker)
    table2 = [0] * len(sticker)
    # table1 : 맨 앞 스티커 사용 / table2 : 두번째 스티커부터 사용
    table1[0] = sticker[0]
    table1[1] = sticker[0]
    for i in range(2, len(sticker)-1):
        table1[i] = max(table1[i-1], table1[i-2]+sticker[i])
    
    table2[1] = sticker[1]
    for j in range(2, len(sticker)):
        table2[j] = max(table2[j-1], table2[j-2]+sticker[j])
    
    answer = max(max(table1), max(table2))
    return answer