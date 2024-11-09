Princpal = int(input("Enter Amaunt of princpal"))
Rate = int(input("Enter The Intrest Rate"))
Time = int(input("Enter The Time"))


def simpal_intrest(Pri=Princpal, Rat=Rate, Tim=Time):
    SI = Pri * Rat * Tim / 100
    print(SI)
    return SI

simpal_intrest()
