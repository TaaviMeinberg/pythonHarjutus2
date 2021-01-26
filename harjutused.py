# Harjutus 1 - Leia vahemik
# Looge funktsioon, mis võtab sisendiks ühe arvu
# Funktsioon peab kontrollima, kas antud arv kuulub vahemikku 0 kuni 100 või 101 kuni 1000
    # Kui kuulub vahemikku 0 kuni 100, siis tuleb printida tekst "Arv on vahemikus 0st 100ni".
    # Kui kuulub vahemikku 101 kuni 1000, siis tuleb printida tekst "Arv on vahemikus 101st 1000ni".

def h1():
    arv = 0
    if arv >= 0 and arv <= 100:
        print('Arv on vahemikus 0st 100ni')
    elif arv > 100 and arv <= 1000:
        print('Arv on vahemikus 101st 1000ni')

h1()


# Harjutus 2 - prindi negatiivsed arvud
# Ette on antud arvude list
arvud = [5, 9, 1, -2, 6, -15, -20]

# Looge funktsioon, mis käib tsükliga kõik arvud listis läbi ning iga arvu puhul kontrollib, kas arv on negatiivne.
    # Kui arv on negatiivne, siis printige see välja

def h2():
    for arv in arvud:
        if arv < 0:
            print(arv)

h2()


# Harjutus 3 - boonus
# Looge funktsioon, mis võtab sisendiks listi, mis koosneb 4st täis arvust.
# Funktsioon peab iga listi elemendi puhul printima uuele reale nii mitu $ sümbolit kui elemendi väärtus ütleb

# Näiteks listi sisend = [1, 3, 4, 3] puhul prinditakse järgnev tulemus
#$
#$$$
#$$$$
#$$$

arvud2 = [1, 3, 4, 3]

def h3():
    for arvud in arvud2:
        print('$' * arvud)


h3()

#H4
#Palun luua funktsioon, mis genereerib etteantud pikkusega parooli, mis koosneb suvalistest tähtedest ja sümbolitest.
#Tähed võivad olla suvaliselt kas suured või väikesed tähed.

import random, string

def h4():
    parooliPikkus = int(input('Sisesta parooli pikkus positiivse täisarvuna: '))
    parooliKarakterid = string.ascii_letters + string.digits + string.punctuation
    parool = []
    for arv in range(parooliPikkus):
        parool.append(random.choice(parooliKarakterid))
    print(''.join(parool))
h4()