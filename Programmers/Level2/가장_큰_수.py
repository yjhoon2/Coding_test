def solution(numbers):
    num = [(str(x), str(x)*3) for x in numbers]
    num.sort(key = lambda x : x[1], reverse = True)
    return str(int(''.join(map(lambda x : x[0], num))))