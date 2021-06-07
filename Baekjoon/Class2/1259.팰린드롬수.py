import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

# 풀이 1
import sys
for line in sys.stdin:
    if int(line) == 0:
        break
    if int(line) == int(line[::-1]) :
        print("yes")
    else:
        print("no")


# 풀이 2
import sys
input=sys.stdin.readline
while 1:
  s=input().rstrip()
  if s=='0': break
  print('yes' if s==s[::-1] else 'no')