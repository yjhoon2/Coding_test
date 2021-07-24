def solution(phone_book):
    dict = {}
    for x in phone_book:
        dict[x] = 0
    for x in phone_book:
        temp = ''
        for i in x:
            temp += i
            if temp in dict and temp != x:
                return False
    else:
        return True
