def h1():
    # Harjutus 1 - Leia vahemik
    # Looge funktsioon, mis võtab sisendiks ühe arvu
    # Funktsioon peab kontrollima, kas antud arv kuulub vahemikku 0 kuni 100 või 101 kuni 1000
        # Kui kuulub vahemikku 0 kuni 100, siis tuleb printida tekst "Arv on vahemikus 0st 100ni".
        # Kui kuulub vahemikku 101 kuni 1000, siis tuleb printida tekst "Arv on vahemikus 101st 1000ni".
    sisestatud_arv = int(input("Sisestage arv: "))
    if sisestatud_arv >= 0 and sisestatud_arv <= 100:
        print("Arv on vahemikus 0st 100ni")
    elif sisestatud_arv >= 101 and sisestatud_arv <= 1000:
        print("Arv on vahemikus 101st 1000ni")
    else:
        print("Error")


def h2():
    # Harjutus 2 - prindi negatiivsed arvud
    # Ette on antud arvude list
    arvud = [5, 9, 1, -2, 6, -15, -20]

    # Looge funktsioon, mis käib tsükliga kõik arvud listis läbi ning iga arvu puhul kontrollib, kas arv on negatiivne.
        # Kui arv on negatiivne, siis printige see välja
    for x in arvud:
        if x < 0:
            print(x)

def h3():
    # Harjutus 3 - boonus
    # Looge funktsioon, mis võtab sisendiks listi, mis koosneb 4st täis arvust.
    # Funktsioon peab iga listi elemendi puhul printima uuele reale nii mitu $ sümbolit kui elemendi väärtus ütleb

    # Näiteks listi sisend = [1, 3, 4, 3] puhul prinditakse järgnev tulemus
    #$
    #$$$
    #$$$$
    #$$$
    sisend = [1, 3, 4, 3, 9, 13]

    for x in sisend:
        väljund = ""
        while x > 0:
            x = x-1
            väljund = väljund + "$"
        print(väljund)

def h4():
    # Harjutus 4 - boonus boonus
    # Palun luua funktsioon, mis genereerib etteantud pikkusea parooli, mis koosneb suvalistest tähtedest ja sümbolitest.
    # Tähed võivad suvaliselt olla kas suured või väikesed tähed

    import random
    kõik_tähed= "abcdefghijklmnopqrsšzžtuvwõäöüxyABCDEFGHIJKLMNOPQRSŠZŽTUVWÕÄÖÜXY"
    parooli_pikkus = int(input("Kui pikka parooli tahate?"))
    vastus = ""
    for x in range(parooli_pikkus):
        vastus = vastus + random.choice(kõik_tähed)
    print(vastus)



h1()

h2()

h3()

h4()

