from collections import Counter
import re
def solution(s):
    ans = Counter(re.findall("\d+", s))
    ans = ans.most_common()
    ans.sort(key = lambda x:x[1], reverse = True)
    res = []
    for x in ans:
        res.append(int(x[0]))
    
    '''
    splited = s[2:-2].split("},{")
    splited.sort(key = lambda x : len(x))
    ans = []
    for x in splited:
        ans = [(int(num) for num in x.split(","))]
    ''' 
    
    
    return res