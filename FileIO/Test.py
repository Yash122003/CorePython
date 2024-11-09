# f = open("My Name.txt", "w")
# f.write("Hello my name is Yash")
# print("done")
# print(f.read())
# f.close()

#
# f = open("My Name.txt","r")
# text = f.read()
# print(text)
# f.close()
#
#
# myfile = open("C:/Users/rajes/OneDrive/Desktop/My Collection.txt","w")
# myfile.write("Photos""\n""Video")
# print("done")
# myfile.close()
#


folder = open("C:/Users/rajes/OneDrive/Desktop/My Collection.txt", "r+")
folder.write("hello")
folder.seek(0)
file = folder.read()
print("file")

folder.close()
