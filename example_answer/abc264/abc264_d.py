import sys
input = sys.stdin.readline

at_dict = dict([(c,i) for i, c in enumerate("atcoder")])
s = list(input().strip())

ans = 0
while s != list("atcoder"):
    index = 0
    while index <= 5:
        if at_dict[s[index]] < at_dict[s[index+1]]:
            index += 1
        else:
            ans += 1
            tmp = s[index]
            s[index] = s[index+1]
            s[index+1] = tmp

print(ans)