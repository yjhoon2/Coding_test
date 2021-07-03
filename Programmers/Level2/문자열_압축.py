def solution(s):
    answer = 21470000
    for i in range(1, len(s)//2 + 2):
        string = [s[j:j+i] for j in range(0, len(s), i)]

        ans = ''
        cnt = 1
        for k in range(1, len(string)):
            if string[k-1] == string[k]:
                cnt += 1
            else:
                ans += (str(cnt)+string[k-1]) if cnt > 1 else string[k-1]
                cnt = 1
        ans += (str(cnt)+string[k-1]) if cnt > 1 else string[-1]

        if len(ans) < answer:
            answer = len(ans)

    return answer