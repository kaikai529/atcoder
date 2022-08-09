import sys
input = sys.stdin.readline

n, k = map(int, input().split())

def g1(a):
    g = list(str(a))
    g.sort(reverse=True)
    return int("".join(g))

def g2(a):
    g = list(str(a))
    g.sort()
    return int("".join(g))

def f(a):
    return g1(a)-g2(a)

ans = n
for i in range(k):
    ans = f(ans)

print(ans)