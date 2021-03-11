from  potrebne_funkce import *

if __name__ == '__main__':


    jmeno = input("Zadej jméno"" ")
    prijmeni = input("Zadej příjmení"" ")
    kontrola_pismen(jmeno, prijmeni)
    mezera()

    vek = int(input("Zadej svůj věk: "))
    kontrola_veku()
    mezera()

    email = input("Zadej emailovou adresu: ")
    kontrola_emailu()
    mezera()

    print("Vaše údaje jse zadal v pořádku mužete začít nakupovat")



