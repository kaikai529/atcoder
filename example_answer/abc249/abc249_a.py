import sys
input = sys.stdin.readline

a, b, c, d, e, f, x = map(int, input().split())

takahashi = a*b*(x//(a+c)) + b*min(x%(a+c), a)
aoki = d*e*(x//(d+f)) + e*min(x%(d+f),d)

if takahashi < aoki: print("Aoki")
elif takahashi==aoki: print("Draw")
else: print("Takahashi")