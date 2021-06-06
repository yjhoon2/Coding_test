import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

word = input()

# a-z : 97-122
for i in range(97, 123):
    if chr(i) in word:
        print(word.index(chr(i)), end = ' ')
    else:
        print(-1, end = ' ')