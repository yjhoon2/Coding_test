import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

# 풀이 1
for i in range(int(input())):
    result = input()
    score = 0
    sub_score = 0
    for j in range(len(result)):
        if result[j] == "O":
            sub_score += 1
            score += sub_score
        else:
            sub_score = 0
    print(score)


# 풀이 2
for i in range(int(input())):
    result = input().rstrip().split("X")
    score = 0
    for j in range(len(result)):
        score += sum(range(len(result[j]) + 1))
    print(score)