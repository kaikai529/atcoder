import sys
input = sys.stdin.readline

n, w = map(int, input().split())
stp = [list(map(int, input().split())) for _ in range(n)]

# 0, max(t)までのリスト
t = [t for _,t,_ in stp]
water = [0]*(max(t)+1)

# 必要な水
for s, t, p in stp:
    water[s] += p
    water[t] -= p 

#　累積和
cum_water = [water[0]]
for i in range(1,len(water)): cum_water.append(cum_water[-1]+water[i])

if max(cum_water) <= w: print("Yes")
else: print("No")