# Harjutus 1 - Leia vahemik
# Looge funktsioon, mis võtab sisendiks ühe arvu
# Funktsioon peab kontrollima, kas antud arv kuulub vahemikku 0 kuni 100 või 101 kuni 1000
    # Kui kuulub vahemikku 0 kuni 100, siis tuleb printida tekst "Arv on vahemikus 0st 100ni".
    # Kui kuulub vahemikku 101 kuni 1000, siis tuleb printida tekst "Arv on vahemikus 101st 1000ni".


# Harjutus 2 - prindi negatiivsed arvud
# Ette on antud arvude list
#arvud = [5, 9, 1, -2, 6, -15, -20]

# Looge funktsioon, mis käib tsükliga kõik arvud listis läbi ning iga arvu puhul kontrollib, kas arv on negatiivne.
    # Kui arv on negatiivne, siis printige see välja


# Harjutus 3 - boonus
# Looge funktsioon, mis võtab sisendiks listi, mis koosneb 4st täis arvust.
# Funktsioon peab iga listi elemendi puhul printima uuele reale nii mitu $ sümbolit kui elemendi väärtus ütleb

# Näiteks listi  puhul prinditakse järgnev tulemus
#$
#$$$
#$$$$
#$$$
sisend = [1, 3, 4, 3]
def h3 (sisend):
    for arv in sisend:
        print('$' * arv)
h3(sisend)
#print('E' * 7)








#H1.

def number (arv):
    if arv > 0 and arv < 100:
        print ("Arv on vahemikus 0st 100ni")
    elif arv > 101 and arv < 1000:
        print ("Arv on vahemikus 101st 1000ni")
number(5)

#H2.

arvud = [5, 9, 1, -2, 6, -15, -20]

for arv in arvud:
    if arv < 0:
        print(arv)


#H3



