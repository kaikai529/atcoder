import sys
input = sys.stdin.readline

sx, sy, tx, ty = map(int, input().split())

# first approch
print("U"*(ty-sy)+"R"*(tx-sx),end="")
print("D"*(ty-sy)+"L"*(tx-sx),end="")

# second approch
print("L"+"U"*(ty-sy+1)+"R"*(tx-sx+1)+"D",end="")
print("R"+"D"*(ty-sy+1)+"L"*(tx-sx+1)+"U")