import sys
input = sys.stdin.readline

a, b, k = map(int, input().split())

this_slimes = a
ans = 0
while this_slimes < b:
    this_slimes *= k
    ans += 1

print(ans)
