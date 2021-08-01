# 혼자 품 ㅎ
def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j-1 >= 0 and j+1 <= len(triangle[i-1]):
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
            elif j-1 >= 0:
                triangle[i][j] += triangle[i-1][j-1]
            elif j+1 <= len(triangle[i-1]):
                triangle[i][j] += triangle[i-1][j]
                
    return max(triangle[-1])