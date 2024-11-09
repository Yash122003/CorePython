class fruits:
    def __init__(self):
        self.price = 100
        self._bags = 5


    def display(self):
        print(self._bags)
        print(self.price)
        print()



obj = fruits()
obj.display()
