def eratosthenes(n):
     # 1. vytvořit seznam čísel od 2 do n včetně
     seznam_cisel = []
     for i in range(2, n+1):
          seznam_cisel.append(i)

     # 2. vytvořit prázdný seznam prvočísel
     prvocisla = []

     # 3. dokud nedojdou čísla v seznamu:
     while len(seznam_cisel) > 0:
          # vezmeme první číslo ze seznamu
          cislo = seznam_cisel[0]
          
          # a smažeme ho v seznamu
          seznam_cisel.remove(cislo)  # smazání pomocí hodnoty
          
          # vložíme ho do seznamu prvočísel
          prvocisla.append(cislo)

          j = 0
          while j < len(prvocisla) - 1:
               if cislo % prvocisla[j] == 0:
                    # smažeme násobek čísla
                    prvocisla.pop()
                    break
               else:
                    # přejdeme na následující pozici
                    j += 1

     # 4. vrátíme seznam prvočísel
     return prvocisla

cislo = int(input("zadej přirozené číslo"))
vysledek = eratosthenes(cislo)
print(f"Výsledek: {vysledek}")