# Definice slovníku pro hodnoty x a y pro jednotlivé svaly
hodnoty_svalu = {
    1: {'x': 3, 'y': 2},
    2: {'x': 5, 'y': 7},
    3: {'x': 1, 'y': 4},
    4: {'x': 8, 'y': 6},
    5: {'x': 2, 'y': 9}
}

# Funkce pro výpočet hodnoty x * sval[i] - y pro daný sval
def vypocet_rovnice(sval_i):
    x = hodnoty_svalu[sval_i]['x']
    y = hodnoty_svalu[sval_i]['y']
    vysledek = x * sval_i - y
    return vysledek

# Příklad použití funkce pro sval č. 3
sval_3_vysledek = vypocet_rovnice(3)
print(f'Hodnota pro sval č. 3: {sval_3_vysledek}')
