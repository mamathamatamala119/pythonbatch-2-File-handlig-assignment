#program for get number of characters, words, spaces and lines in a file
file = open("python.txt","r")
data = file.read()
nc = 0
nw = 0
ns = 0
nl = 0
for i in data:
    if i == " ":
        ns=ns+1
    else:
        nc=nc+1
print("no of spaces:",ns)
print("no of characters:",nc)
for i in data.split():
    nw=nw+1
print("no of words:",nw)
file=open("python.txt","r")
line=file.readlines()

for i in line:
    nl=nl+1
print("no of lines:",nl)
file.close()