import sys
input = sys.stdin.readline
# 自作ライブラリ


def IN():
    return map(int, input().split())


def STR_IN():
    return input().strip()


def INs(n: int):
    return [map(int, input().split()) for _ in range(n)]

# main


o = STR_IN()
e = STR_IN()

ans = ""
for _o, _e in zip(o, e):
    ans = ans + _o + _e

if len(o) - len(e):
    print(ans + o[-1])
else:
    print(ans)
