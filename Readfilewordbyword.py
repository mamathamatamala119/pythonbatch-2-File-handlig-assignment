#f = open("python.txt","w")
#f.write("python is easy to learn")
with open("python.txt","r")as file:
    for line in file:
        for word in line.split():
            print(word)