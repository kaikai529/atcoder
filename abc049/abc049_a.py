import sys
input = sys.stdin.readline

s = set(["a", "i", "u", "e", "o", input().strip()])

if len(s)==5: print("vowel")
else: print("consonant")
