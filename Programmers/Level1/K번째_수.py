def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        a = commands[i][0]
        b = commands[i][1]
        k = commands[i][2]
        
        new_array = array[a-1:b]
        new_array.sort()
        answer.append(new_array[k-1])
        
    return answer