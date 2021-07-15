def solution(str1, str2):
    arr1 = []
    arr2 = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            arr1.append(str1[i:i+2].lower())
    
    for j in range(len(str2)-1):
        if str2[j].isalpha() and str2[j+1].isalpha():
            arr2.append(str2[j:j+2].lower())

    a = list(set(arr1) & set(arr2)) # 교집합
    b = list(set(arr1) | set(arr2)) # 합집합

    aa = sum([min(arr1.count(x), arr2.count(x)) for x in a])
    bb = sum([max(arr1.count(x), arr2.count(x)) for x in b])
    
    if aa == 0 and bb == 0:
        return 65536
    else:
        return int(aa/bb*65536)


## 정규표현식 쓴것
import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)