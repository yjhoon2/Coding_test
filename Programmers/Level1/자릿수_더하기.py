def solution(n):
    answer = 0
    while n != 0:
        answer += n % 10
        n = n // 10
    return answer


# 재귀함수로 만들기
def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10) # 재귀함수 안에서 함수 호출 가능.