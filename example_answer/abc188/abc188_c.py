import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

left_a = a[:2**(n-1)]
right_a = a[2**(n-1):]

left_max = 0
left_index = 0
for i, a_ in enumerate(left_a):
    if left_max < a_:
        left_max = a_
        left_index = i

right_max = 0
right_index = 0
for i, a_ in enumerate(right_a):
    if right_max < a_:
        right_max = a_
        right_index = i

if left_max < right_max: print(left_index+1)
else: print(2**(n-1)+right_index+1)