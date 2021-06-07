import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
words = [input().rstrip() for _ in range(n)]

words = list(set(words))
#print(sorted(words, key = lambda x : (len(x), x)))

words.sort(key = lambda x : (len(x), x))
#print(words)
for i in range(len(words)):
    print(words[i])