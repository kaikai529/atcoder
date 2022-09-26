import sys
input = sys.stdin.readline
## 自作ライブラリ
def IN():
    return map(int, input().split())

def INs(n: int):
    return [map(int, input().split()) for _ in range(n)]

## main

a, b, c = IN()
if b-a == c-b:
    print("YES")
else:
    print("NO")