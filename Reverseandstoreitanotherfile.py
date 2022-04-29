#python program to reverse the content of a file and storeit in another filw
f1=open("reversefile.txt","w")
with open("test.txt","r")as file:
    data=file.read()
    r=data[::-1]
f1.write(r)
f1.close()
with open("reversefile.txt","r")as f:
    data=f.read()
    print(data)