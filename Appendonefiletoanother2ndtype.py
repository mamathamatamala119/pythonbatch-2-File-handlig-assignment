#python program to append content one file to another
file1=open("abcd.txt","a")
file2=open("python.txt","r")
s=set()
for line in file2:
    file1.write(line)
    s.add(line)
print(s)
file1.close()
file2.close()