from random import randint, choice

samohlasky = "aáeéiíoóuúůyý"
souhlasky = "qwrtzpsdfghjklxcvbnmščřž"
počet = 0

while True:
    try:
        print("\n")
        pocetslov = int(input("Vložte počet slov:   "))
        break
    except ValueError:
        print("\n")
        print("Takhle ne ...")
        
print("\n")
nazevsouboru = input("Zvolte jméno souboru:   ")
with open (nazevsouboru, "w") as f:
    for _ in range(pocetslov):
        if počet > 70:
            f.write("\n")
            počet = 0   
        slovo = ""
        delka = randint(1,7)
        zacatek = randint(0,1)
        for i in range(delka):
            if i % 2 == zacatek:
                slovo += choice(samohlasky)
            else:
                slovo += choice(souhlasky)
        f.write(slovo)
        počet = počet + len(slovo) + 1
        if počet > 70:
            f.write("")
        else:
            f.write(" ")