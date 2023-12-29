f=open("nagasiva.txt","w")


a=open("jagan.txt","w")


b=open("shanwith.txt","w")


c=open("students.csv","w")





#zipfile


from zipfile import *





f=ZipFile("python.zip","w")


f.write("nagasiva.txt")


f.write("jagan.txt")


f.write("shanwith.txt")


f.write("students.csv")


f.close()


print("zip file  created")








# #unzip file


from zipfile import *


f=ZipFile("python.zip","r")


n=f.namelist()


print(n)


for i in n:


    print("filename=",i)


    #how to read a file


    f1=open(i,"r")


    print(f1.read())


    print()








import os


cwd=os.getcwd()


print("msg",cwd)





# #how to create folder


import os


cwd=os.mkdir("ramu/python")








# # #multiple sub directiories


import os


cwd=os.makedirs("file1/file2/file3/file4")








# #one file in multiple files


import os


os.mkdir("file1/good")


os.mkdir("file1/fine")


os.mkdir("file1/super")


os.mkdir("file1/awesome")





os.rmdir("file1/good")#file is empty is deleted





# # how to multiple files deleted--only sub directories deleted


os.removedirs("file1/file2/file3/file4")





import os


print(os.listdir("ramu"))








import os


print(os.listdir("desktop"))





import os


print(os.listdir("."))





import os


print(os.listdir("15-11-23 list datastructures"))