# a = int(input("Enter Value Of A :"))
# b = int(input("Enter Value Of B :"))
# if a>b:
#     print(a)
# else:
#     print(b)
#
#
# a= ["Y","A","S","H"]
# print(a)
# a.reverse()
# print(a)

# a = int(input("Enter a value of a :"))
# b = int(input("Enter a value of b :"))
# c = int(input("Enter a value of c :"))
# if a < b:
#     if a < c:
#         print(a)
#     else:
#         print(c)
# else:
#     print(b)
#
#
# a = int(input("Enter a value of a"))
# b = int(input("Enter a value of b"))
# a = a + b
# b = a - b
# a = a - b
# print(a)
# print(b)


class Car:
    def __init__(self, Bmw, Audi):
        self.B = Bmw
        self.A = Audi

    def Bmw(self):
        return self.B

    def Audi(self):
        return self.A


obj = Car("B1","A1")
print("Car:",obj.Bmw(),obj.Audi())
