import os.path

Fname = "test.bmp"
hhfp = open(Fname + ".hhmn","rb")
hifp = open(Fname + ".himn","r")
#txtfp = open(Fname ,"w+b")

siz = os.path.getsize(Fname + ".hhmn")

Htable = {}

for lop in hifp:
    data = hifp.readline()
    cha , num = data.split(",")
    num = num.strip("\n")
    Htable[ cha ] = num

print(siz)
cnt = int(siz/10)
for lop in range(siz):
    if lop > cnt :
        print("read " + str( int(cnt / int(siz/10)) ) +"/ 10")
        cnt += int(siz/10)


hhfp.close()
hifp.close()
#txtfp.close()