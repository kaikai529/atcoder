import sys
input = sys.stdin.readline

down = "0"
flag = [False]*7
cols = [[6],[3],[1,7],[0,4],[2,8],[5],[9]]
s = input().strip()

if s[0] != down:
    print("No")
    exit()

for col_idx, col in enumerate(cols):
    for pin_num in col:
        if s[pin_num] != down:
            flag[col_idx] = True
            break

for left_idx in range(6):
    if not (flag[left_idx] and not flag[left_idx+1]):
        continue
    for right_idx in range(left_idx+2,7):
        if flag[right_idx]:
            print("Yes")
            exit()
print("No")
