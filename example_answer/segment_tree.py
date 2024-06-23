# モノイドの設定
def operator(x,y):
    return x+y

# セグメント木
class segtree:

    def __init__(self, n,operator,init_val=0):
        """
        n:データ配列のサイズ
        operator:演算子(モノイド)。関数オブジェクト
        identity:演算子に対応する単位元
        """
        
        self.num_leaves = 1<<(n-1).bit_length()
        self.data = [init_val for _ in range(self.num_leaves * 2)] #単位元で初期化

        self.identity = init_val 
        self.operator = operator
        
    def update(self,x,val):
        """
        x:代入位置
        val:代入する値
        """
        actual_x = x+self.num_leaves #1-indexの末端の葉のindexがどこから始まるか分を足す(例えばデータ配列サイズ4のとき木配列サイズは8で、後半部はindex4から始まる。
        self.data[actual_x] = val #値を更新する
        while actual_x > 0 :
            actual_x = actual_x//2#親を見る
            self.data[actual_x] = self.operator(self.data[actual_x*2],self.data[actual_x*2+1])#あたらしい子をつかって親を更新



st = segtree(5, operator)
st.update(1,1)
print(st.data)