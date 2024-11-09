# Car Model
#
# class Car:
#     def __init__(self, Make, Model, Year):
#         self.Make = Make
#         self.Model = Model
#         self.Year = Year
#
#     def make(self):
#         return self.Make
#
#     def model(self):
#         return self.Model
#
#     def year(self):
#         return self.Year
#
#
# obj = Car("BMW", 2018, 2024)
# print("Car:", obj.make(),"\nModel:",obj.Model,"\nYear:",obj.Year )
#
#
# Mobile Battery
#
# class Mobile:
#
#     def __init__(self, maH, percent):
#         self.maH = maH
#         self.percent = percent
#
#     def maH(self):
#         return self.maH
#
#     def percent(self):
#         return self.percent
#
#
# class Battery(Mobile):
#
#     def battery(self, maH, percent):
#         super().battery(maH)
#         super().battery(percent)
#
#
# obj = Battery(6000, 90)
# print("Battery maH:", obj.maH, "\nBattery %", obj.percent)
#
#
# Bank Account
#
# class Bank:
#     def __init__(self, totalbalance, accountNO, depositamound, withdraw):
#         self.totalbalance = totalbalance
#         self.accountNO = accountNO
#         self.dipositamound = depositamound
#         self.withdraw = withdraw
#
#     def gettotal(self):
#         return self.totalbalance
#
#     def getaccount(self):
#         return self.accountNO
#
#     def grtde(self):
#         return self.dipositamound
#
#     def getdiposit(self):
#         return self.totalbalance + self.dipositamound
#
#
# class withdraw:
#
#     def getwithdraw(self):
#         return self.withdraw
#
#     def getw(self):
#         return self.totalbalance - self.withdraw
#
#
# D = Bank(10000, "ANJ2003", 5000, 3000)
# print()
