import sys
input = sys.stdin.readline

k = int(input())
hh = 21 + k//60
mm = 0 + k%60

if mm < 10: print(str(hh)+":"+ "0"+str(mm))
else: print(str(hh)+":"+str(mm))