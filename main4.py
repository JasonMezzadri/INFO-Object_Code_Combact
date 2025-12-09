from classe_personaggio4 import Personaggio
from classe_arma4 import Arma
from classe_pozione4 import Pozione
import random

if __name__ == "__main__":
    print("=== SIMULAZIONE COMBATTIMENTO — PARTE 4 ===\n")

    # ------------------------------------------------------
    # CREAZIONE PERSONAGGI
    # ------------------------------------------------------
    try:
        p1 = Personaggio("Gimli", 50, random.randint(8, 18), random.randint(8, 18))
        p2 = Personaggio("Legolas", 45, random.randint(8, 18), random.randint(8, 18))
    except ValueError as e:
        print(f"Errore nella creazione dei personaggi: {e}")
        exit()

    print(f"{p1.nome}: Forza={p1.forza}, Destrezza={p1.destrezza}")
    print(f"{p2.nome}: Forza={p2.forza}, Destrezza={p2.destrezza}\n")

    # ------------------------------------------------------
    # EQUIPAGGIO ARMI
    # ------------------------------------------------------
    try:
        if p1.forza >= p1.destrezza:
            arma1 = Arma("Spada a due mani", 8, 15, "mischia")
        else:
            arma1 = Arma("Arco", 6, 12, "distanza")
        p1.equip(arma1)
    except (ValueError, TypeError) as e:
        print(f"Errore equipaggiando arma a {p1.nome}: {e}")

    try:
        if p2.forza >= p2.destrezza:
            arma2 = Arma("Ascia", 8, 14, "mischia")
        else:
            arma2 = Arma("Balestra", 8, 13, "distanza")
        p2.equip(arma2)
    except (ValueError, TypeError) as e:
        print(f"Errore equipaggiando arma a {p2.nome}: {e}")

    # ------------------------------------------------------
    # POZIONI
    # ------------------------------------------------------
    try:
        cura1 = Pozione("Pozione di Cura", "cura", 15)
        cura2 = Pozione("Pozione di Cura", "cura", 15)
        cura3 = Pozione("Pozione di Cura", "cura", 15)
        cura4 = Pozione("Pozione di Cura", "cura", 15)

        if p1.forza >= p1.destrezza:
            buff1 = Pozione("Pozione della Forza", "buff_forza", 3, 3)
        else:
            buff1 = Pozione("Pozione della Destrezza", "buff_destrezza", 3, 3)

        if p2.forza >= p2.destrezza:
            buff2 = Pozione("Pozione della Forza", "buff_forza", 3, 3)
        else:
            buff2 = Pozione("Pozione della Destrezza", "buff_destrezza", 3, 3)

        p1.pozioni = [cura1, cura2, buff1]
        p2.pozioni = [cura3, cura4, buff2]

    except (ValueError, TypeError) as e:
        print(f"Errore nella creazione delle pozioni: {e}")
        exit()

    # ------------------------------------------------------
    # COMBATTIMENTO
    # ------------------------------------------------------
    turno = 1
    while p1.e_vivo() and p2.e_vivo():
        print(f"--- Turno {turno} ---")

        # TURNO P1
        try:
            poz = p1.decidi_se_usare_pozione(p2)
            if poz:
                print(f"{p1.nome} usa {poz.nome}!")
                p1.usa_pozione(poz)
        except Exception as e:
            print(f"Errore nell’uso della pozione di {p1.nome}: {e}")

        try:
            danno1 = p1.attacca(p2)
            print(f"{p1.nome} attacca {p2.nome} e infligge {danno1} danni!")
        except Exception as e:
            print(f"Errore nell’attacco di {p1.nome}: {e}")

        print(p2, "\n")
        if not p2.e_vivo():
            break

        # TURNO P2
        try:
            poz = p2.decidi_se_usare_pozione(p1)
            if poz:
                print(f"{p2.nome} usa {poz.nome}!")
                p2.usa_pozione(poz)
        except Exception as e:
            print(f"Errore nell’uso della pozione di {p2.nome}: {e}")

        try:
            danno2 = p2.attacca(p1)
            print(f"{p2.nome} attacca {p1.nome} e infligge {danno2} danni!")
        except Exception as e:
            print(f"Errore nell’attacco di {p2.nome}: {e}")

        print(p1, "\n")

        # Aggiorna buff
        p1.aggiorna_buff()
        p2.aggiorna_buff()
        turno += 1

    # RISULTATI
    print("=== FINE COMBATTIMENTO ===\n")
    if not p1.e_vivo() and not p2.e_vivo():
        print("Pareggio! Entrambi cadono in battaglia.")
    elif p1.e_vivo():
        print(f"🏆 {p1.nome} vince! {p1}")
    else:
        print(f"🏆 {p2.nome} vince! {p2}")
