"""
木構造の全探索
https://qiita.com/myumura/items/141dafed1f34b03413f9
"""
import sys
sys.stdin.readline

def dfs(depth, pos):
    print(depth, pos)
    for i in tree[pos]:
        dfs(depth+1, i)


# リストを用いた木構造
tree = [[1, 2, 3], [4, 5], [], [6, 7], [8, 9], [], [10], [], [], [], []]
dfs(0, 0)