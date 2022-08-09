import sys
input = sys.stdin.readline

n = int(input())
x = map(int, input().split())

man, eu, che = 0, 0, 0

for x_ in x:
    man += abs(x_)
    eu += x_**2
    che = max(che, abs(x_))

print(man)
print(eu**0.5)
print(che)