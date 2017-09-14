secreto = "holi"
secretox = ""
secretoxx = ""
secretoxxx = ""
i = 1

secretox = input("Escribe la palabra secreta.")

while i == 1:

    if secretox.lower() != secreto:
        print("intenta de nuevo")
        secretoxx = input("Escribe la palabra secreta.")
    else:
        print("ganaste")
        break

    if secretoxx.lower() != secreto:
        print("intenta de nuevo")
        secretoxxx = input("Escribe la palabra secreta.")
    else:
        print("ganaste")
        break

    if secretoxxx.lower() != secreto:
        print("perdiste")
        break
    else:
        print("ganaste")
        break





