"""
整数a1,a2,...,anから複数選び、和がkとなるか判定
"""
import sys
input = sys.stdin.readline

n = 9
a = [1,2,4,7]
k = 13

def dfs(depth:int, sum:int)->bool:
    # エンドケース => n個選択した時にsumを返す
    if depth==n:
        return sum==k

    # 分岐条件 => a[depth]を使わない or a[depth]を使う
    if dfs(depth+1, sum+0): 
        return True
    if dfs(depth+1, sum+a[depth]): 
        return True

    # その他
    return False

print(dfs(0,0))



