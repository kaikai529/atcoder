import sys
input = sys.stdin.readline

abc = input().strip()

abcabc = abc*2
ans = int(abc)
for i in range(2):
    ans += int(abcabc[i+1:i+4])

print(ans)
