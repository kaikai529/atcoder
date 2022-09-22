from collections import Counter
import sys
input = sys.stdin.readline

bin_n = bin(int(input()))[2:]
cnt_1 = Counter(bin_n)["1"]

for comb in range(2**cnt_1):    
    idx = 0
    ans = ""
    for bin_i in bin_n[::-1]:
        if bin_i == "1":
            ans = str(comb>>idx&1) + ans
            idx += 1
        else:
            ans = "0" + ans
    print(int("0b" + ans, 2))

 
