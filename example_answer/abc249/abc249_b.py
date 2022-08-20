import sys
input = sys.stdin.readline

string = input().strip()

case1 = False
case2 = False
case3 = set()
for s in string:
    if ord("A") <= ord(s) <= ord("Z"):
        case1 = True
    if ord("a") <= ord(s) <= ord("z"):
        case2 = True
    case3.add(s)

if case1 and case2 and (len(string)==len(case3)): print("Yes")
else: print("No")
