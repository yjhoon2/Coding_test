from collections import defaultdict
def solution(genres, plays):
    answer = []
    music = defaultdict(list)
    music_len = {}
    for i, [x, y] in enumerate(zip(genres, plays)):
        music[x].append([y, i])
        music_len[x] = music_len.get(x, 0) + y
    
    for m in music.keys():
        music[m].sort(key = (lambda x : (x[0], -x[1])), reverse = True)
    
    #music_len = sorted(music_len, key = (lambda x : x[1]), reverse = True)
    music_len = sorted(music_len.items(), key = (lambda x : x[1]), reverse = True)
    
    for g in music_len:
        cnt = 0
        for n in music[g[0]]:
            if cnt == 2:
                break
            else:
                cnt += 1
                answer.append(n[1])
    return answer