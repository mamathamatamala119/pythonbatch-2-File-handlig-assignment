#
File1 = "python.txt"
File1 = open(File1, 'r')
File2 = "abcd.txt"
File2 = open(File2,'w')
gvn_prefix = input("Enter some random prefix = ")
for lines in File1 .readlines(): 

    if not (lines.startswith(gvn_prefix)): 
        print(lines)  
        File2.write(lines) 
File2.close() 
File1.close()