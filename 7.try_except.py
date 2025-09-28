x = input("Introduceti un numar")
print("Ai introdus:", x)
print(type(x))

try:
    x = int(x)
    print("Numarul poate fi transformat")
    print(type(x))
except:
    print("Nu se poate transforma in int!!!!")

