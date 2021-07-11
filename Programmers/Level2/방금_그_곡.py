def change(mel):
    if 'C#' in mel:
        mel = mel.replace('C#', 'c')
    if 'D#' in mel:
        mel = mel.replace('D#', 'd')
    if 'F#' in mel:
        mel = mel.replace('F#', 'f')
    if 'A#' in mel:
        mel = mel.replace('A#', 'a')
    if 'G#' in mel:
        mel = mel.replace('G#', 'g')
    return mel

def solution(m, musicinfos):
    answer = ("(None)",0)
    m = change(m)
    
    for i in range(len(musicinfos)):
        musicinfos[i] = change(musicinfos[i])
            
        music = musicinfos[i].split(',')
        
        start = music[0].split(':')
        end = music[1].split(':')
        time = (int(end[0]) - int(start[0]))*60 + int(end[1]) - int(start[1])
        
        if len(music[3]) >= time:
            melody = music[3][:time]
        else:
            melody = (music[3]*time)[:time]
        
        if m in melody:
            if time > answer[1]:
                answer = (music[2], time)
            
    return answer[0]