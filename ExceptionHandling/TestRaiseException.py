try:
    number = int(input("Enter Your Number:"))
    if number>10:
        raise Exception("invalid number")
except Exception as e:
    print(e)