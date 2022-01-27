alfabeto = ["a", "b", "c", "d", "e", "f",
            "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r",
            "s", "t", "u", "v", "w", "x",
            "y", "z"]

text = input("Digite um texto:\n")
stringFinal = ""

for letra in text:
    if letra in alfabeto:
        indiceOrg = alfabeto.index(letra)
        letraFinal = (indiceOrg + 3) %26
        stringFinal += alfabeto[letraFinal]
    else:
        stringFinal += letra
    
print(f"Texto final:\n {stringFinal}")
