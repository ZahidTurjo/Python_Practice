# f1=open("file_1.txt","w+")

# f1.write('i am tuRjo. ')
# f1.write("i am front end web developer")
# f1.seek(0)
# print(f1.read())
# f1.close()
f1=open("file_1.txt","a+")
f1.write(". how r u?")
print(f1.tell())
f1.seek(0)
print(f1.read())


