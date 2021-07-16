## 정답
def solution(n, t, m, p):
    dict = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    answer = ''
    for num in range(t*m):
        # 이거 넣으니까 틀리고 divmod하니까 정답 됨...
        #a = num // n
        #b = num % n
        a, b = divmod(num, n)
        if b >= 10:
            ans = dict[b]
        else:
            ans = str(b)
        while a > 0:
            #a = a//n
            #b = a%n
            a, b = divmod(a, n)
            if b >= 10:
                ans = dict[b] + ans
            else:
                ans = str(b)+ans
        answer += ans
    
    res = ''
    for i in range(p-1, len(answer), m):
        res += answer[i]
    
    return res[:t]