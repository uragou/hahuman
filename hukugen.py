import os.path

Fname = "1.pdf"
hhfp = open(Fname + ".hhmn","rb")
hifp = open(Fname + ".himn","r")
txtfp = open(Fname ,"w+b")

siz = os.path.getsize(Fname + ".hhmn") 

Htable = {}

def fufile(strbin):
    nowbin = ""
    for lop in range( len(strbin) ):
        nowbin = nowbin + strbin[lop]
        if nowbin in Htable:
            wribin = Htable[ nowbin ]
            txtfp.write( int(wribin , 2).to_bytes(1, byteorder='big') )
            nowbin = ""
    
    return nowbin

data = hifp.readline()
while data:
    cha , num = data.split(",")
    num = num.strip("\n")

    cha = str( bin( int(cha[1:]) ) )
    cha = cha[2:]
    while len(cha) < 8 :
        cha = "0" + cha 
        
    Htable[ num ] = cha
    data = hifp.readline()
cnt = int(siz/10)

strbyte = ""

for lop in range( siz ):
    if lop > cnt :
        print("read " + str( int(cnt / int(siz/10)) ) +"/ 10")
        cnt += int(siz/10)

    bite = hhfp.read(1)

    lopbyte = bin( int.from_bytes(bite , "big") ) 
    lopbyte = lopbyte[2:] 
    while len(lopbyte) < 8 :
        lopbyte = "0" + lopbyte

    strbyte = strbyte + lopbyte
    strbyte = fufile(strbyte)

hhfp.close()
hifp.close()
txtfp.close()