import sys
input = sys.stdin.readline

x = input().strip()

if "." in x:
    ans, _ = x.split(".")
    print(ans)
else:
    print(x)