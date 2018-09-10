import os.path

fp = open("test","rb")

siz = os.path.getsize("test")
Btable = {}
Htable = {}

for lop in range(siz):
    data = fp.read(1)

    Bget = "b" + str(ord(data))

    if Bget in Btable:
        Btable[Bget] = Btable[Bget] + 1
    else:
        Btable[Bget] = 1

print(Btable)
print(len(Btable))
print(max(Btable.values()))
BStable = sorted(Btable.items() , key = lambda x:x[1] , reverse = True)
print(BStable)
fp.close()