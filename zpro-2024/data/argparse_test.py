import argparse

# Vytvoření parseru
parser = argparse.ArgumentParser(description='Program pro výpočet součtu a rozdílu.')

# Přidání argumentů
# poziční argumenty
parser.add_argument('cislo1', type=int, help='První číslo pro výpočty')
parser.add_argument('cislo2', type=int, help='Druhé číslo pro výpočty')

# nepovinne argumenty s libovolnym umistenim
parser.add_argument('-s', '--soucet', action='store_true', help='Spočítat součet čísel')
parser.add_argument('-r', '--rozdil', action='store_true', help='Spočítat rozdíl čísel')

# Zpracování příkazové řádky
args = parser.parse_args()

# Výpočty na základě přijatých argumentů
if args.soucet:
    vysledek = args.cislo1 + args.cislo2
    print(f'Součet: {vysledek}')
if args.rozdil:
    vysledek = args.cislo1 - args.cislo2
    print(f'Rozdíl: {vysledek}')
if not args.soucet and not args.rozdil:
    print('Není vybrána žádná operace.')
