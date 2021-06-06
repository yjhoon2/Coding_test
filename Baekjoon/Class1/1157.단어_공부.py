import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

word = input()
word = word.lower()

word_list = list(set(word))
answer = ''
cnt = []
for i in range(len(word_list)):
    cnt.append(word.count(word_list[i]))

if cnt.count(max(cnt)) == 1:
    print(word_list[cnt.index(max(cnt))].upper())
else:
    print("?")

