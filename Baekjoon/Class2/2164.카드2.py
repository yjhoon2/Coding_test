import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

from collections import deque

n = int(input())
cards = list(range(1, n+1))
cards = deque(cards)
while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())
print(cards[0])