import sys
input = sys.stdin.readline

s = input().strip()
a, b = map(int, input().split())

ans = []
for i in range(len(s)):
    if i==a-1:
        ans.append(s[b-1])
    elif i==b-1:
        ans.append(s[a-1])
    else:
        ans.append(s[i])

print("".join(ans))
