import sys
input = sys.stdin.readline

n, C = map(int, input().split())

event = []
for i in range(n):
    a, b, c = map(int, input().split())
    event.append([a, c])
    event.append([b+1, -c])

event.sort()

ans = 0
fee = 0
now = 0

#　いもす法の改良版
for x, y in event:
    if now != x:
        ans += min(C,fee)*(x-now)
        now = x
    fee+=y

print(ans)