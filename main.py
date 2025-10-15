from classe_personaggio import Personaggio
from classe_arma import Arma
import random

if __name__ == "__main__":
    # Creiamo due personaggi con valori casuali
    p1 = Personaggio("Eroe", 20, random.randint(1, 20), random.randint(1, 20))
    p2 = Personaggio("Mostro", 20, random.randint(1, 20), random.randint(1, 20))

    # Assegnazione delle armi in base alla caratteristica dominante
    if p1.forza >= p1.destrezza:
        arma1 = Arma("Spada", 3, 8, "mischia")
    else:
        arma1 = Arma("Arco", 2, 6, "distanza")
    p1.equipaggia(arma1)

    if p2.forza >= p2.destrezza:
        arma2 = Arma("Ascia", 3, 8, "mischia")
    else:
        arma2 = Arma("Balestra", 2, 6, "distanza")
    p2.equipaggia(arma2)

    print(f"\nCombattimento tra {p1.nome} e {p2.nome}!")
    print(f"{p1.nome} usa {p1.arma}")
    print(f"{p2.nome} usa {p2.arma}\n")

    turno = 1
    #Ciclo finché entrambi sono vivi
    while p1.e_vivo() and p2.e_vivo():
        print(f"--- Turno {turno} ---")

        danno1 = p1.attacca(p2)
        print(f"{p1.nome} infligge {danno1} danni a {p2.nome}. ({p2})")

        if not p2.e_vivo():
            break  

        danno2 = p2.attacca(p1)
        print(f"{p2.nome} infligge {danno2} danni a {p1.nome}. ({p1})\n")

        turno += 1

    # Risultato finale
    if not p1.e_vivo() and not p2.e_vivo():
        print("Entrambi sono morti! Pareggio.")
    elif p1.e_vivo():
        print(f"\n{p1.nome} vince!")
    else:
        print(f"\n{p2.nome} vince!")