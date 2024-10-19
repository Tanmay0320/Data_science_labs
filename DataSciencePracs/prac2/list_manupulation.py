def readnames(li):
    f=open("names.txt")
    li.append(f.read())
    #for i in f:
    #    i=i.replace("\n","")
    #    li.append(str(i))
    f.close()
     
def loadInMatrix(li1,li2):
    li2.extend(li1[0].strip().split("\n"))
    for i in range(len(li2)):
        li1.append(li2[i])

def covertToColumnMajor(li):
    n = max([len(i) for i in li])
    li2=[]
    for i in range(n):
        x=""
        for j in range(len(li)):
            try:
                x+=li[j][i]
            except:
                x+=" "
        li2.append(x.rstrip())
    li.clear()
    li.extend(li2)    
    
def calculateCharacterLength(li):
    length=0
    for i in li:
        length+=len(i.replace(" ",""))
    print("total length:"+str(length))
    
def storeListAsString(li):
    covertToColumnMajor(li)
    file=open("output.txt",'wt')
    for i in li:
        file.write(i.strip())
    print("file created")

def main():
    a=[]
    b=[]
    c=[]
    d=[]
    readnames(a)
    print("read names:")
    print(a)
    loadInMatrix(a,b)
    print("load in matrix:")
    print(b)
    c=b
    covertToColumnMajor(c)
    print("convert to column major:")
    print(c)
    calculateCharacterLength(b)
    d=b
    storeListAsString(d)
    
main()

file=open("output.txt",'r')
print("output length:")
print(len(file.read()))