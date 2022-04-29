#python program to read character to character from a file
file = open("python.txt","r")
while 1:
    char = file.read(1)
    if not char:
        break
    print(char)
file.close()