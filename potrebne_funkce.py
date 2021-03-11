from konzum_produkty import *

print("Vítejte v aplikaci obchodní společnosti Chleba.cz. Zadejte zakladni informace a pak Vám umožníme nakupavat.")

def mezera():
    print("_" * 80)


def kontrola_pismen():
    while True:
        jmeno = input("Zadej jméno: ")
        prijmeni = input("Zadej příjmení: ")
        if jmeno.isalpha() and prijmeni.isalpha():
            print("Zadal jsi správně")
            break
        else:
            print("Jméno a příjmení musí obsahovat pouze písmena")
            continue

def kontrola_veku():
    while True:
        vek = int(input("Zadej svůj věk: "))
        if vek >= 12:
            print("Pokračuj v zadávání emailu")
            break
        else:
            print("Nemáš dostatek let k nakupování. Nashledanou")

def kontrola_emailu():
    email = input("Zadej emailovou adresu: ")
    if "@" and "." not in email:
        print("Oprav email")

    else:
        print("Můžeš pokračovat k nakupování")

print(mezera)
kontrola_pismen()
print(mezera)
kontrola_veku()
print(mezera)
kontrola_emailu()
print(mezera)



nakupni_kosik = []
ucet = []

while True:
    vyber_produktu = input(
        "Zadejte druh produktu, který si chcete koupit ( ovoce, zelenina). Pro ukončení nakupování stiskni (q): ").lower()
    if vyber_produktu == "q":
        print("Chcete ukončit nakupování")
        break
    nakup = muj_konzum.get(vyber_produktu, "Nemáme")
    if nakup == "Nemáme":
        print("Tento produkt nemáme")
        continue
    else:
        print("Můžeš vybírat z těchto produktů:", list(nakup.keys()))
        konkretni_produkt = input("Zadej konkrétní produkt: ")
        nakupni_kosik.append(konkretni_produkt)
        cena = nakup.get(konkretni_produkt, 0)
        if cena == 0:
            print("Produkt nenáme")
        else:
            ucet.append(cena)

def rozlouceni(jmeno, prijmeni, nakupni_kosik, ucet):
    rozlouceni = f""" V obchodě nakupoval {jmeno}, {prijmeni}, nakoupil {nakupni_kosik}, v celkové hodnotě {sum(ucet)} Kč"""
    print(rozlouceni)

rozlouceni(jmeno, prijmeni, nakupni_kosik, ucet)
exit()
