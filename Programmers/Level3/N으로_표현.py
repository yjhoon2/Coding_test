## 와 이 방법 생각하는거 미쳤네...
# 혼자 못 품...
def solution(N, number):
    memo = []
    for i in range(1, 9):
        case = set()
        case.add(int(str(N)*i))
        for j in range(i-1):
            for a in memo[j]:
                for b in memo[-j-1]:
                    case.add(a + b)
                    case.add(a - b)
                    case.add(a * b)
                    if b != 0:
                        case.add(a // b)
        if number in case:
            return i
        memo.append(case)
    else:
        return -1