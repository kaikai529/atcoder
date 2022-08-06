import sys
input = sys.stdin.readline

n = int(input())

# 順列{a=n}のn項項までの総和
print((1+n)*n//2)