def solution(numbers, hand):
    answer = ''
    hand_L = 10
    hand_R = 12
    for i in numbers:
        if i in [1, 4, 7]:
            answer += "L"
            hand_L = i
        elif i in [3, 6, 9]:
            answer += "R"
            hand_R = i
        else:
            if i == 0:
                i = 11
            len_L = sum(divmod(abs(i - hand_L), 3))
            len_R = sum(divmod(abs(i - hand_R), 3))
            if len_L < len_R:
                answer += "L"
                hand_L = i
            elif len_L > len_R:
                answer += "R"
                hand_R = i
            else:
                if hand == "right":
                    answer += "R"
                    hand_R = i
                else: 
                    answer += "L"
                    hand_L = i
            
    return answer