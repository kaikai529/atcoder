import sys
input = sys.stdin.readline

a, b = map(int, input().split())

a_sum, b_sum = 0, 0
for i in range(3):
    a_sum += a%10
    a //= 10
    b_sum += b%10
    b //= 10

print(max(a_sum, b_sum))