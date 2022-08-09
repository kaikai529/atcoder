""" 考え方
自然数のみで考え、それを2倍する
"""
from operator import xor
import sys
input = sys.stdin.readline

n = int(input().strip())

while n%2==0:
    n//=2

sq = int(n**0.5)
ans = sum(n%i for i in range(1,sq+1))*2 - (sq*sq==n)

print(ans*2)
    
