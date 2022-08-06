""" 考え方
今回はXX or XYX となる部分配列があるがどうかを
探索することで十分である

理由
5以上の部分配列は2と3を組み合わせることで実現できる
そのため、2と3と4の時を考える
2のとき XXのみ
3のとき XXY, YXX（2と重複する）, XYX
4のとき 三つ以上が同じ数でなければならないため
        全て同じまたはひとつ異なる（これは2,3と重複する）
"""
import sys
input = sys.stdin.readline

s = input().strip()

# |s|が2の場合
if len(s)==2 and s[0]==s[1]:
    print("1 2")
    exit()

# |s|が3以上の場合
for i in range(len(s)-2):
    if s[i]==s[i+1]:
        print(str(i+1)+" "+str(i+2))
        exit()
    elif s[i]==s[i+2]:
        print(str(i+1)+" "+str(i+3))
        exit()

print("-1 -1")