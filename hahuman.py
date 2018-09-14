import os.path
import numpy

Fname = "test"
ifp = open(Fname,"rb")

siz = os.path.getsize("test")
Btable = {}
Htable = []
Wtable = None
Hnum = 0

#木構造したい
class HTree:
    def __init__(self,lf,ri,sm):

        self.oya = None
        self.left  = lf
        self.right = ri
        self.hi = sm

    def __str__(self): 
        return str( self.oya )

#2つデータとを取ってそいつを木にしたい。
#途中で木が複数できたり統合したりする関係でおかしなことになっている
#奇数のときには一つ目のデータを取っている部分のため、ここでデータが一つしかないかを判断する
#２つ目の部分ではデータが複数個あるのは確定なので木にしている

#終了条件 元のテーブルが空になって木を入れた配列の長さが１のとき
#つまりは全てのデータが一つの木に入った時
#if文のそれぞれは
"""
    1. 木がある無い場合
    1.1 元データが一種しかない場合 : そのまま木にデータにぶち込む　(多分整合性エラー)
    1.2 元データが複数ある場合    
    2. 元データが無くて、木がある場合 :　木の中で色々する
    3. 両方ある場合
"""
def MakeTree(TBL):
    print(Htable)
    Itree = []
    cnt = 0

    if not Htable:
        print("not data")
        return 
    while True:
        cnt += 1
        if not(Itree):
            if len(Htable) == 1:
                Itree.append(Htable)
                break
            else:
                buf1 = min( Htable )
                Htable.remove( min( Htable ) )
        elif not(Htable):
            if len(Itree) == 1:
                break
            buf1 = min( Itree )
        else:
            print("Ibuf")
            print( Itree )
            print( min( Itree ) )
            print("Ibuf")
            Ibuf = min( Itree )
            buf1 = min( Htable  )
            
            if Ibuf[0] < buf1[0]:
                buf1 = Ibuf
                Itree.remove( min( Itree ) )
            else :
                Htable.remove( min( Htable ) )
                    
        if not(Itree):
            buf2 = min( Htable )
            Htable.remove( min( Htable ) )
            Tbuf = HTree(buf1[1] , buf2[1] , buf1[0] + buf2[0] )
            Itree.append( [  Tbuf.hi , Tbuf ] )
        elif not(Htable):
            buf2 = min( Itree )
            Itree.remove( min( Itree ) )
            Tbuf = HTree(buf1[1] , buf2[1] , buf1[0] + buf2[0] )
            Itree.append( [  Tbuf.hi , Tbuf ] )
        else:
            Ibuf = min( Itree )
            buf1 = min( Htable  )
            if Ibuf[0] < buf1[0]:
                buf2 = Ibuf
                Itree.remove( min( Itree ) )
            else :
                Htable.remove( min( Htable ) )
            Tbuf = HTree(buf1[1] , buf2[1] , buf1[0] + buf2[0] )
            Itree.append( [  Tbuf.hi , Tbuf ] )
        print("-----------------------------")
        for lop in range(len(Itree)):
            print(Itree[lop])
        print( cnt )

    print("-----------------------------")
    for lop in range(len(Itree)):
        print(Itree)

#データ取り出し部分
#１バイトごと取って数を数えている
for lop in range(siz):
    data = ifp.read(1)

    Bget = "b" + str(ord(data))

    if Bget in Btable:
        Btable[Bget] = Btable[Bget] + 1
    else:
        Btable[Bget] = 1

#ソート部分
#print(Btable)
#print(len(Btable))
#print(max(Btable.values()))
BStable = sorted(Btable.items() , key = lambda x:x[1])
#print(BStable)

#単純に数えていたバイト列を出現率に変えている
for lop in range( len( BStable ) ):
    Htable.append( [ Btable[ BStable[lop][0] ] / siz , BStable[lop][0] ] )
    
MakeTree(Htable)

ofp = open(Fname + ".hhmn" , "wb")
ifp.seek(0)

"""
for lop in range(siz):
    data = ifp.read(1)

    Bget = "b" + str(ord(data))
    print(Bget)
    print(Htable[ Bget ])
    print( bin(Htable[ Bget ]) )
    ofp.write( bin(Htable[ Bget ]) )
"""

ifp.close()
ofp.close()