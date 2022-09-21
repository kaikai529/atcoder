import sys
input = sys.stdin.readline

n, q = map(int, input().split())
array = [i+1 for i in range(n)]
index = [i for i in range(n+1)]

for _ in range(q):
    x = int(input())
    x_index = index[x]-1
    if x_index == n-1:
        left_x = array[x_index-1]
        # swap index
        index[x] -= 1
        index[left_x] += 1
        # swap array
        array[-1] = left_x
        array[-2] = x
    else:
        right_x = array[x_index+1]
        # swap index
        index[x] += 1
        index[right_x] -= 1
        # swap array
        array[x_index] = right_x
        array[x_index+1] = x

print(*array)