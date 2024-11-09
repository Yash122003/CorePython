# import pickle
#
#
# class Employe:
#     def __init__(self, eno, ename, city, age):
#         self.eno = eno
#         self.ename = ename
#         self.city = city
#         self.age = age
#
#
# e = Employe(1, "Yash", "Barwani", 21)
# f = open("C:/Users/rajes/OneDrive/Desktop/emp.txt", "wb")
# pickle.dump(e, f)
# f.close()
#
# f= open("C:/Users/rajes/OneDrive/Desktop/emp.txt", "rb")
# e= pickle.load(f)
# f.close()
# print(e.eno)
# print(e.ename,e.city,e.age)


file = open("C:/Users/rajes/OneDrive/Desktop/Yash.txt","w")
text = "Hii"
while (text != "quit"):
    text = input("Enter your text")
    file.write(text)
    file.write("\n")
    if (text == "quit"):
        break


file.close()
