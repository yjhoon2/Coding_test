import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n, m = map(int, input().split())
mat = [list(input().rstrip()) for _ in range(n)]

result = []

for i in range(n-7):
    for j in range(m-7):
        W = 0
        B = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b)%2 == 0:
                    if mat[a][b] != "W":
                        W += 1
                    if mat[a][b] != "B":
                        B += 1
                else:
                    if mat[a][b] != "B":
                        W += 1
                    if mat[a][b] != "W":
                        B += 1
        result.append(W)
        result.append(B)
print(min(result))