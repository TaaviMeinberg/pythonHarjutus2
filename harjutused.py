# Harjutus 1 - Leia vahemik
# Looge funktsioon, mis võtab sisendiks ühe arvu
# Funktsioon peab kontrollima, kas antud arv kuulub vahemikku 0 kuni 100 või 101 kuni 1000
    # Kui kuulub vahemikku 0 kuni 100, siis tuleb printida tekst "Arv on vahemikus 0st 100ni".
    # Kui kuulub vahemikku 101 kuni 1000, siis tuleb printida tekst "Arv on vahemikus 101st 1000ni".



# Harjutus 2 - prindi negatiivsed arvud
# Ette on antud arvude list
arvud = [5, 9, 1, -2, 6, -15, -20]

# Looge funktsioon, mis käib tsükliga kõik arvud listis läbi ning iga arvu puhul kontrollib, kas arv on negatiivne.
    # Kui arv on negatiivne, siis printige see välja


# Harjutus 3 - boonus
# Looge funktsioon, mis võtab sisendiks listi, mis koosneb 4st täis arvust.
# Funktsioon peab iga listi elemendi puhul printima uuele reale nii mitu $ sümbolit kui elemendi väärtus ütleb

# Näiteks listi sisend = [1, 3, 4, 3] puhul prinditakse järgnev tulemus
#$
#$$$
#$$$$
#$$$



#ül.1

def arvud(võrreldavarv):
    if (võrreldavarv > 100 and võrreldavarv < 1000):
        print('arv on vahemikus 101st 1000ni')
    elif (võrreldavarv > 0 and võrreldavarv <= 100):
        print('arv on vahemikus 0st 100ni')


arvud(500)



#ül.2
def negatiivnearv():

    list = [5, 9, 1, -2, 6, -15, -20]
    for arv in list:
        if arv < 0:
            print(arv)


negatiivnearv()

def täisarv():
    list2 = [1, 3, 4, 3]
    for x in list2:
        print ("$" * x)
täisarv()