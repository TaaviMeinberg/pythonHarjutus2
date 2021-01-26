# Harjutus 1 - Leia vahemik
# Looge funktsioon, mis võtab sisendiks ühe arvu
# Funktsioon peab kontrollima, kas antud arv kuulub vahemikku 0 kuni 100 või 101 kuni 1000
    # Kui kuulub vahemikku 0 kuni 100, siis tuleb printida tekst "Arv on vahemikus 0st 100ni".
    # Kui kuulub vahemikku 101 kuni 1000, siis tuleb printida tekst "Arv on vahemikus 101st 1000ni".


#h1
def ül1():
    arv=int(input('Sisestage arv'))
    if arv >= 0:
        print('Arv on vahemikus 0-100')
    if arv>=101 and arv<1000:
        print('Arv on 101-1000')

#ül1()


# Harjutus 2 - prindi negatiivsed arvud
# Ette on antud arvude list
arvud = [5, 9, 1, -2, 6, -15, -20]

# Looge funktsioon, mis käib tsükliga kõik arvud listis läbi ning iga arvu puhul kontrollib, kas arv on negatiivne.
    # Kui arv on negatiivne, siis printige see välja

#h2
def ül2():
    for arv in arvud:
        if arv<0:
            print(arv, 'Arv on negatiivne')
        else:
            print(arv,'Arv ei ole negatiivne')

#ül2()


# Harjutus 3 - boonus
# Looge funktsioon, mis võtab sisendiks listi, mis koosneb 4st täis arvust.
# Funktsioon peab iga listi elemendi puhul printima uuele reale nii mitu $ sümbolit kui elemendi väärtus ütleb

# Näiteks listi sisend = [1, 3, 4, 3] puhul prinditakse järgnev tulemus
#$
#$$$
#$$$$
#$$$

#h3

arvud2 = [5, 9, 1, 2, 6, 15, 20]
for arv2 in arvud2:
    print('$'*arv2)


#h4
#Palun luua funktsioon, mis genereerib etteantud pikkusega parooli, mis koosneb suvalistest tähtedest ja sümbolitest.
#Tähed võivad suvaliselt olla kas suured või väikesed tähed

import random
def parooliTegeja(14):
    tähestikJaNum=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','1','2','3','4','5','6','7','8','9','0']
    count=0
    coinFlip = random.randrange(2)
    parool=[]
    while count<arv3:
        suvaline = random.randint(1, len(tähestikJaNum))



        parool.append(tähestikJaNum[suvaline])
        count=count+1
    print(parool)


parooliTegeja(25)



