from threading import Thread

class Hii(Thread):
    def run(self):
        for i in range(500):
            print("Hii",i)

t1=Hii()
t1.start()