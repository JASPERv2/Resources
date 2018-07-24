import os
j=20

#while True :
file=open("testfile"+str(j)+".txt","w")
os.system("espeak "+"what..........your------name")
print("input your name")
name=raw_input()
os.system("espeak "+"input-----your------age")
print("input your age")
age=raw_input()
os.system("espeak "+"input-----your------place")
print("input your place")
place=raw_input()

file=open("testfile"+str(j)+".txt","w")
file.write(name)
file.write(age)
file.write(place)

file.close()

