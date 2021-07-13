def solution(w,h):
    w1=w 
    h1=h
    while(w1!=h1):#유클리드 호제법
        if w1>h1:#W1이 더크면 w1에서 h1을 빼준다
            w1-=h1
        else:   #h1이 더크면 반대
            h1-=w1
    
    return w*h-(w+h-h1) #h1 이든 w1 이든 같음