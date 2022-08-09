import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]
wv.sort(key=lambda x:x[1], reverse=True)
x = list(map(int, input().split()))
x = [(x_, i) for i, x_ in enumerate(x)]
x.sort()
query = list(map(int, input().split()) for _ in range(q))

for l, r in query:
    ans = 0
    box = x.copy()
    for w, v in wv:
        for j, (x_, i) in enumerate(box):
            if l-1 <= i <= r-1: continue
            if w>x_: continue
            ans += v
            box.pop(j)
            break
    print(ans)