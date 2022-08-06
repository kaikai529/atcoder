import sys
input = sys.stdin.readline

s = input().strip()

ans = ""
for s_ in s:
    if s_=="0":
        ans += "0"
    elif s_=="1":
        ans += "1"
    elif s_=="B":
        ans = ans[:-1]

print(ans)