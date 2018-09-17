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
    def __init__(self,lval,lname,rval,rname,oya = None):

        self.oya = oya
        self.lval  = lval
        self.lname = lname
        self.rval  = rval
        self.rname = rname
        if not (lval == None and rval == None ):
            self.hi = lval + rval
        else:
            self.hi = None

    def __str__(self): 
        return str( self.oya )

    def Lmarge(self,lval,lname,rnode):
        root = HTree(lval,lname,rnode.hi,"edge")
        rnode.oya = root 
        return root

    def Rmarge(self,lnode,rval,rname):
        root = HTree(lnode.hi,"edge",rval,rname)
        lnode.oya = root 
        return root

    def marge(self,lnode,rnode):
        root = HTree(lnode.hi,"edge",rnode.hi,"edge")
        rnode.oya = root 
        lnode.oya = root 
        return root




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
    Itree = []
    cnt = 0

    if not TBL:
        print("not data")
        return 
    while True:
        if not Itree:
            if len(TBL) == 1:
                Itree = TBL
                break
            else:
                Tbuf = HTree(TBL[0][0] , TBL[0][1] , TBL[1][0] , TBL[1][1])
                TBL.remove(TBL[1])
                TBL.remove(TBL[0])
                Itree.append( [Tbuf.hi , Tbuf] )
        else:
            if not TBL:
                if len(Itree) == 1:
                    break
                else:
                    Tbuf = HTree(None,None,None,None)
                    Tbuf = Tbuf.marge(Itree[0][1],Itree[1][1])
                    Itree.remove(Itree[1])
                    Itree.remove(Itree[0])
                    Itree.append( [Tbuf.hi , Tbuf] )
            else:
                if len(Itree) == 1 and len(Htable) == 1 :
                    buf1 = TBL[0]
                    buf2 = Itree[0]
                    Itree.remove(Itree[0])
                    TBL.remove(TBL[0])

                    Tbuf = HTree(None,None,None,None)
                    Tbuf = Tbuf.Rmarge(buf1[0],buf1[1],buf2[1])
                    Itree.append( [Tbuf.hi , Tbuf] )
                else :
                    if Itree[0][0] > TBL[0][0]:
                        buf1 = Itree[0]
                        Itree.remove(Itree[0])

                        if not Itree:
                            buf2 = TBL[0]
                            TBL.remove(TBL[0])

                            Tbuf = HTree(None,None,None,None)
                            Tbuf = Tbuf.Rmarge(buf1[1],buf2[0],buf2[1])
                            Itree.append( [Tbuf.hi , Tbuf] )

                        elif Itree[0][0] > TBL[0][0]:
                            buf2 = Itree[0]
                            Itree.remove(Itree[0])

                            Tbuf = HTree(None,None,None,None)
                            Tbuf = Tbuf.marge(buf1[1],buf2[1])
                            Itree.append( [Tbuf.hi , Tbuf] )
                        else:
                            buf2 = TBL[0]
                            TBL.remove(TBL[0])

                            Tbuf = HTree(None,None,None,None)
                            Tbuf = Tbuf.Lmarge(buf1[1],buf2[0],buf2[1])
                            Itree.append( [Tbuf.hi , Tbuf] )

                    else:
                        buf1 = TBL[0]
                        TBL.remove(TBL[0])

                        if not TBL:
                            buf2 = Itree[0]
                            Itree.remove(Itree[0])
                            Tbuf = HTree(None,None,None,None)
                            Tbuf = Tbuf.Lmarge(buf1[0],buf1[1],buf2[1])
                            Itree.append( [Tbuf.hi , Tbuf] )
                        elif Itree[0][0] > TBL[0][0]:
                            buf2 = Itree[0]
                            Itree.remove(Itree[0])

                            Tbuf = HTree(None,None,None,None)
                            Tbuf = Tbuf.Rmarge(buf1[0],buf1[1],buf2[1])
                            Itree.append( [Tbuf.hi , Tbuf] )
                        else:
                            buf2 = TBL[0]
                            TBL.remove(TBL[0])

                            Tbuf = HTree(buf1[0] , buf1[1] , buf2[0] , buf2[1])
                            Itree.append( [Tbuf.hi , Tbuf] )
        cnt += 1
        if cnt == 100 :
            break
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