import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
movie = 666
while n:
    if "666" in str(movie):
        n -= 1
    movie += 1
print(movie-1)

