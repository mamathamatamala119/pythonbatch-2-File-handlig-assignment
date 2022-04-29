#python program to merge two files into a third file
d1=d2=" "
f1=open("test.txt","r")
d1=f1.read()
f2=open("test2.txt","r")
d2=f2.read()
d1+="\n"
d1+=d2
f3=open("mergefile.txt","w")
f3.write(d1)
f1.close()
f2.close()
with open("mergefile.txt","r")as f:
    data=f.read()
    print(data)