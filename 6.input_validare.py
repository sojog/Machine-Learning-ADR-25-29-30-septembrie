
x = input("Introduceti un numar")
print("Ai introdus:", x)
print(type(x))

if x.isnumeric():
    x = int(x)
    print("Numarul poate fi transformat")
    print(type(x))
else:
    print("Nu se poate transforma in int!!!!")



