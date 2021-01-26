# Harjutus 1 - Leia vahemik
# Looge funktsioon, mis võtab sisendiks ühe arvu
# Funktsioon peab kontrollima, kas antud arv kuulub vahemikku 0 kuni 100 või 101 kuni 1000
    # Kui kuulub vahemikku 0 kuni 100, siis tuleb printida tekst "Arv on vahemikus 0st 100ni".
    # Kui kuulub vahemikku 101 kuni 1000, siis tuleb printida tekst "Arv on vahemikus 101st 1000ni".
def vahemik (võrraArv):
    if võrraArv > 0 and võrraArv < 100:
        print('Arv on vahemikus 0st 100ni')
    elif võrraArv > 101 and võrraArv < 1000:
        print('Arv on vahemikus 101st 100ni')
vahemik(33)

# Harjutus 2 - prindi negatiivsed arvud
# Ette on antud arvude list
arvud = [5, 9, 1, -2, 6, -15, -20]

# Looge funktsioon, mis käib tsükliga kõik arvud listis läbi ning iga arvu puhul kontrollib, kas arv on negatiivne.
    # Kui arv on negatiivne, siis printige see välja
def negArvud():
    for neg in arvud:
        if neg < 0:
            print(neg)
negArvud()
# Harjutus 3 - boonus
# Looge funktsioon, mis võtab sisendiks listi, mis koosneb 4st täis arvust.
# Funktsioon peab iga listi elemendi puhul printima uuele reale nii mitu $ sümbolit kui elemendi väärtus ütleb

# Näiteks listi sisend = [1, 3, 4, 3] puhul prinditakse järgnev tulemus
#$
#$$$
#$$$$
#$$$
sisend = [1, 3, 4, 3]
def listBoonus():
    for listUus in sisend:
        #print(sisend)
        #print(listUus)
        print('$'* listUus)

listBoonus()

#print('Ä' * 9)
#print('Ä' * 3)
