dict = {'name':"anant", 'age':19}
k=input("Enter key to search:")
d=dict.keys()
try:
    v=dict[k]
    print("key is present")
except Exception:
    print("key not found")
