from classe_personaggio2 import Personaggio
from classe_arma2 import Arma
import random

if __name__ == "__main__":
    print("=== SIMULAZIONE COMBATTIMENTO ===\n")

    # Creazione dei personaggi
    p1 = Personaggio("Gimli", 50, random.randint(8, 18), random.randint(8, 18))
    p2 = Personaggio("Legolas", 45, random.randint(8, 18), random.randint(8, 18))

    print(f"{p1.get_nome()}: Forza={p1.get_forza()}, Destrezza={p1.get_destrezza()}")
    print(f"{p2.get_nome()}: Forza={p2.get_forza()}, Destrezza={p2.get_destrezza()}\n")

    # Equipaggiamento automatico in base alla statistica dominante
    if p1.get_forza() >= p1.get_destrezza():
        arma1 = Arma("Spada a due mani", 8, 15, "mischia")
    else:
        arma1 = Arma("Arco", 6, 12, "distanza")
    p1.equipaggia(arma1)

    if p2.get_forza() >= p2.get_destrezza():
        arma2 = Arma("Ascia", 8, 14, "mischia")
    else:
        arma2 = Arma("Balestra", 8, 13, "distanza")
    p2.equipaggia(arma2)

    print(f"{p1.get_nome()} equipaggia: {p1.get_arma()}")
    print(f"{p2.get_nome()} equipaggia: {p2.get_arma()}\n")

    print("=== INIZIO COMBATTIMENTO ===\n")

    turno = 1
    while p1.e_vivo() and p2.e_vivo():
        print(f"--- Turno {turno} ---")
        danno1 = p1.attacca(p2)
        print(f"{p1.get_nome()} attacca {p2.get_nome()} e infligge {danno1} danni!")
        print(p2, "\n")

        if not p2.e_vivo():
            break

        danno2 = p2.attacca(p1)
        print(f"{p2.get_nome()} attacca {p1.get_nome()} e infligge {danno2} danni!")
        print(p1, "\n")

        turno += 1

    print("=== FINE COMBATTIMENTO ===\n")

    # Risultato finale
    if not p1.e_vivo() and not p2.e_vivo():
        print("Pareggio! Entrambi sono caduti in battaglia.")
    elif p1.e_vivo():
        print(f"🏆 {p1.get_nome()} vince il combattimento! {p1}")
    else:
        print(f"🏆 {p2.get_nome()} vince il combattimento! {p2}")