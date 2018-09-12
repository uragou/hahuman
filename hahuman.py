import os.path

Fname = "test"
ifp = open(Fname,"rb")

siz = os.path.getsize("test")
Btable = {}
Htable = []
Wtable = None
Hnum = 0


class HTree:
    def __init__(self,lf,ri,sm):

        self.oya = sm
        self.left  = lf
        self.right = ri

def MakeTree(TBL):
    print(Htable)
    TTable = None
    cnt = 12
    print(Htable[0][0])
    print(Htable[0][1])
    print(Htable[1][0])
    print(Htable[1][1])
    while True:

        cnt+=1
        if cnt == 12:
            break


for lop in range(siz):
    data = ifp.read(1)

    Bget = "b" + str(ord(data))

    if Bget in Btable:
        Btable[Bget] = Btable[Bget] + 1
    else:
        Btable[Bget] = 1

#print(Btable)
#print(len(Btable))
#print(max(Btable.values()))
BStable = sorted(Btable.items() , key = lambda x:x[1])
#print(BStable)

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