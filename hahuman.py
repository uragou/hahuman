import os.path

Fname = "DSCF0002.JPG"
ifp = open(Fname,"rb")

siz = os.path.getsize(Fname)
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

        root = HTree(lval,lname,rnode.hi,rnode)
        rnode.oya = root 
        return root

    def Rmarge(self,lnode,rval,rname):
        root = HTree(lnode.hi,lnode,rval,rname)
        lnode.oya = root 
        return root

    def marge(self,lnode,rnode):
        root = HTree(lnode.hi,lnode,rnode.hi,rnode)
        rnode.oya = root 
        lnode.oya = root 
        return root
    
    def seek(self,tar):
        creData = ""
        
        if self.lname == tar:
            print(self.lname)
            return str(0)
        elif self.rname == tar:
            return str(1)
        else:
            creData = self.lname.subseek(tar,"0")
            if creData == str(-1) :
                creData = self.rname.subseek(tar,"1")
        return creData

    def subseek(self,tar,data):
        if self.lname == tar:
            return data + str(0)
        elif self.rname == tar:
            return data + str(1)
        
        buf = ""
        if not (type(self.lname) is str):
            buf = self.lname.subseek(tar,data + str(0))
            if not (buf == "-1"):
                return  buf
        if not (type(self.rname) is str):
            buf = self.rname.subseek(tar,data + str(1))
            if not (buf == "-1"):
                return  buf
        
        return "-1"
    
    def __str__(self):
        return "edge"



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
    
    lis = TBL[:]

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
                    Tbuf = Tbuf.Rmarge(buf2[1],buf1[0],buf1[1])
                    Itree.append( [Tbuf.hi , Tbuf] )
                else :
                    if Itree[0][0] <= TBL[0][0]:
                        
                        buf1 = Itree[0]
                        Itree.remove(Itree[0])

                        if not Itree:
                            buf2 = TBL[0]
                            TBL.remove(TBL[0])
                            Tbuf = HTree(None,None,None,None)
                            Tbuf = Tbuf.Rmarge(buf1[1],buf2[0],buf2[1])
                            Itree.append( [Tbuf.hi , Tbuf] )

                        elif Itree[0][0] <= TBL[0][0]:
                            
                            buf2 = Itree[0]
                            Itree.remove(Itree[0])

                            Tbuf = HTree(None,None,None,None)
                            Tbuf = Tbuf.marge(buf1[1],buf2[1])
                            Itree.append( [Tbuf.hi , Tbuf] )
                        else:
                            buf2 = TBL[0]
                            TBL.remove(TBL[0])

                            Tbuf = HTree(None,None,None,None)
                            Tbuf = Tbuf.Lmarge(buf2[0],buf2[1],buf1[1])
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
                        elif Itree[0][0] <= TBL[0][0]:
                            buf2 = Itree[0]
                            Itree.remove(Itree[0])

                            Tbuf = HTree(None,None,None,None)
                            Tbuf = Tbuf.Rmarge(buf2[1],buf1[0],buf1[1])
                            Itree.append( [Tbuf.hi , Tbuf] )
                        else:
                            buf2 = TBL[0]
                            TBL.remove(TBL[0])

                            Tbuf = HTree(buf1[0] , buf1[1] , buf2[0] , buf2[1])
                            Itree.append( [Tbuf.hi , Tbuf] )
        cnt += 1

    HAtable = {}
    for lop in range(len(lis)):
        HAtable[ lis[lop][1] ] = Itree[0][1].seek(lis[lop][1]) 
    print(HAtable)
    return HAtable


#データ取り出し部分
#１バイトごと取って数を数えている
print("open " + Fname)

for lop in range(siz):
    data = ifp.read(1)
    Bget = "b" + str(ord(data))

    if Bget in Btable:
        Btable[Bget] = Btable[Bget] + 1
    else:
        Btable[Bget] = 1

BStable = sorted(Btable.items() , key = lambda x:x[1])


#単純に数えていたバイト列を出現率に変えている
for lop in range( len( BStable ) ):
    Htable.append( [ Btable[ BStable[lop][0] ] / siz , BStable[lop][0] ] )

Htable = MakeTree(Htable)
ofp = open(Fname + ".hhmn" , "w+b")
tfp = open(Fname + ".himn" , "w+")
ifp.seek(0)
brry = ""

print("create file 1/2")
while True:
    data = ifp.read(1)
    if not data:
        break
    Bget = "b" + str(ord(data))
    brry += Htable[ Bget ]
    while len(brry) >= 8:
        ofp.write( int(brry[0:8] , 2).to_bytes(1, byteorder='big' ) )
        brry = brry[8:]


print("create file 2/2")
for num , mo in Htable.items():
    tfp.write( num + "," + mo + "\n" )

ifp.close()
tfp.close()
ofp.close()