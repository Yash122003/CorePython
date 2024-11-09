# a = 50
# b = 0
# try:
#     c = a % b
#     print(c)
# except Exception:
#     print("This value cant be module by zero")
#
#
#
#
# a = 40
# b = 0
# try:
#     c = a % b
#     print(c)
# except Exception:
#     print("This value cant be module by zero")
#
# finally:
#     print("Hello always excute")


try:
    d = int(input("Enter Value:"))
    a = '10'
    b = 'a'
    c = a / b
    print(c)
    print(d)
except TypeError as t:
    print("Type Error")
except ValueError as v:
    print("Value Error")
except ModuleNotFoundError as m:
    print("Module Not Found")
