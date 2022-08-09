import sys
input = sys.stdin.readline

n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

a_sum = 0
sub = []
for a, b in ab:
    a_sum += a 
    sub.append(a*2+b)

sub.sort()
for i in range(1, n+1):
    a_sum -= sub[-i]
    if a_sum < 0:
        print(i)
        exit()

