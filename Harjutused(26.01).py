# Harjutus 1 - Leia vahemik
# Looge funktsioon, mis võtab sisendiks ühe arvu
# Funktsioon peab kontrollima, kas antud arv kuulub vahemikku 0 kuni 100 või 101 kuni 1000
    # Kui kuulub vahemikku 0 kuni 100, siis tuleb printida tekst "Arv on vahemikus 0st 100ni".
    # Kui kuulub vahemikku 101 kuni 1000, siis tuleb printida tekst "Arv on vahemikus 101st 1000ni".

a = int(input('sisestage arv '))
if 0 <= a <= 100:
    print('Arv on vahemikus 0st kuni 100ni')
if 101 <= a <= 1000:
    print('Arv on vahemikus 101st 1000ni')
else:
    print('arv on vahemikust 0st kuni 1000 väljas')


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

list = [1, 2, 3, 4]

for arvud in list:
    print('$' * arvud)



# Funktsioon peab iga listi elemendi puhul printima uuele reale nii mitu $ sümbolit kui elemendi väärtus ütleb

# Näiteks listi sisend = [1, 3, 4, 3] puhul prinditakse järgnev tulemus
#$
#$$$
#$$$$
#$$$

print('')

#Harjutus 4

import random
import string

def get_suvaline_string(pikkus):
    tähed = string.ascii_lowercase + string.digits + string.punctuation
    tulemus_str = ''.join(random.choice(tähed) for i in range(pikkus))
    print("Suvaline tekstirida pikkus ", pikkus, "on:", tulemus_str)S

get_suvaline_string(10)
