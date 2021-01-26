# Harjutus 1 - Leia vahemik
# Looge funktsioon, mis võtab sisendiks ühe arvu
# Funktsioon peab kontrollima, kas antud arv kuulub vahemikku 0 kuni 100 või 101 kuni 1000
# Kui kuulub vahemikku 0 kuni 100, siis tuleb printida tekst "Arv on vahemikus 0st 100ni".
# Kui kuulub vahemikku 101 kuni 1000, siis tuleb printida tekst "Arv on vahemikus 101st 1000ni".
number = 1001
if number < 101:
    print("arv on vahemikus 100")
elif number > 100 and number < 1000:
    print("arv on vahemikus 101")
else:
    print("puudub")

# Harjutus 2 - prindi negatiivsed arvud
# Ette on antud arvude list
arvud = [5, 9, 1, -2, 6, -15, -20]

for arv in arvud:
    if arv < 0:
        print(arv)

# Looge funktsioon, mis käib tsükliga kõik arvud listis läbi ning iga arvu puhul kontrollib, kas arv on negatiivne.
# Kui arv on negatiivne, siis printige see välja


# Harjutus 3 - boonus
# Looge funktsioon, mis võtab sisendiks listi, mis koosneb 4st täis arvust.
# Funktsioon peab iga listi elemendi puhul printima uuele reale nii mitu $ sümbolit kui elemendi väärtus ütleb

list = [1, 3, 4, 3]

for point in list:
    print("e" * point)

# Näiteks listi sisend = [1, 3, 4, 3] puhul prinditakse järgnev tulemus
# $
# $$$
# $$$$
# $$$
