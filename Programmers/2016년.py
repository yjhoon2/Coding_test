def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    
    date = sum(month[:a-1]) + b
    d = date%7
    
    return day[d]
