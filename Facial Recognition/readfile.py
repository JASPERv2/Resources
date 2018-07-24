from filemaker import file
import os

j=20
file=open("testfile"+str(j)+".txt","r")
a=file.read()
print(a)
os.system("espeak "+str(a))

#n=True

import splitvdeo
