def solution(arr):
    n = len(arr)
    answer = [0, 0]
    
    def DFS(a, b, m):
        if m == 1:
            if arr[a][b] == 1:
                answer[1] += 1
            else:
                answer[0] += 1
            return
            
        init = arr[a][b]
        flag = False
        for i in range(a, a+m):
            for j in range(b, b+m):
                if arr[i][j] != init:
                    DFS(a, b, m//2)
                    DFS(a, b+m//2, m//2)
                    DFS(a+m//2, b, m//2)
                    DFS(a+m//2, b+m//2, m//2)
                    flag = True
                    break
            if flag:
                break
        else:
            if init == 1:
                answer[1] += 1
            else:
                answer[0] += 1
            
    DFS(0, 0, n)
    return answer