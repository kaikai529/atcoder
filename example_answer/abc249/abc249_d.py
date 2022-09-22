from math import sqrt
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a_box = [0]*(2*10**5+1)
for a_ in a: a_box[a_] += 1

ans = 0
for a_ in a:
    a_sqrt = int(sqrt(a_))
    for i in range(1,a_sqrt+1):
        if a_%i == 0:
            ans += 2*a_box[i]*a_box[a_//i]
    if a_ == a_sqrt**2:
        ans -= a_box[a_sqrt]*a_box[a_sqrt]
print(ans)

