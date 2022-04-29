file=open("python.txt","r")
line=file.readlines()
nl=0
for i in line:
    nl=nl+1
print("no of lines:",nl)
file.close()