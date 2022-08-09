import sys
from tkinter import S
input = sys.stdin.readline

s = input()

if s[-2]=="s":
    print(s[:-1]+"es")
else:
    print(s[:-1]+"s")