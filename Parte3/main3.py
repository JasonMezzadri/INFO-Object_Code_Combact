from classe_personaggio3 import Personaggio
from classe_arma3 import Arma
from classe_pozione3 import Pozione
import random

if __name__ == "__main__":
    print("=== SIMULAZIONE COMBATTIMENTO — PARTE 3 ===\n")

    # ------------------------------------------------------
    # CREAZIONE PERSONAGGI (identica alla tua Parte 2)
    # ------------------------------------------------------

    p1 = Personaggio("Gimli", 50, random.randint(8, 18), random.randint(8, 18))
    p2 = Personaggio("Legolas", 45, random.randint(8, 18), random.randint(8, 18))

    print(f"{p1.nome}: Forza={p1.forza}, Destrezza={p1.destrezza}")
    print(f"{p2.nome}: Forza={p2.forza}, Destrezza={p2.destrezza}\n")

    # ------------------------------------------------------
    # EQUIPAGGIO ARMI (lascia tutto ciò che avevi già)
    # ------------------------------------------------------

    if p1.forza >= p1.destrezza:
        arma1 = Arma("Spada a due mani", 8, 15, "mischia")
    else:
        arma1 = Arma("Arco", 6, 12, "distanza")
    p1.arma = arma1   # <-- ora usi il setter property

    if p2.forza >= p2.destrezza:
        arma2 = Arma("Ascia", 8, 14, "mischia")
    else:
        arma2 = Arma("Balestra", 8, 13, "distanza")
    p2.arma = arma2   # <-- idem

    print(f"{p1.nome} equipaggia: {p1.arma}")
    print(f"{p2.nome} equipaggia: {p2.arma}\n")

    # ------------------------------------------------------
    # AGGIUNTA DELLE POZIONI (NUOVO Parte 3)
    # ------------------------------------------------------

    # # QUI devi dare 3 pozioni a ciascun personaggio:
    # # - 2 pozioni di cura
    # # - 1 pozione di buff coerente con la statistica dominante

    # # esempio struttura:
    # # pozioni_p1 = [Pozione(...), Pozione(...), Pozione(...)]
    # # poi p1.pozioni = pozioni_p1

    # --- p1 ---
    # # 1) pozioni di cura (x2)
    # # 2) buff_forza se forza >= destrezza, altrimenti buff_destrezza

    # --- p2 ---
    # # uguale per p2

    # # ⚠️ ricorda: il setter pozioni deve controllare max 3 e tipo corretto


    print("=== INIZIO COMBATTIMENTO ===\n")

    turno = 1
    while p1.e_vivo() and p2.e_vivo():
        print(f"--- Turno {turno} ---")

        # ------------------------------------------------------
        # TURNO DI p1
        # ------------------------------------------------------
        # # 1. decide se usare una pozione
        # # poz = p1.decidi_se_usare_pozione(p2)
        # # se poz != None → p1.usa_pozione(poz)

        # # 2. attacco come prima
        # danno1 = p1.attacca(p2)
        # print(f"{p1.nome} attacca {p2.nome} e infligge {danno1} danni!")
        # print(p2, "\n")

        if not p2.e_vivo():
            break

        # ------------------------------------------------------
        # TURNO DI p2
        # ------------------------------------------------------
        # # come sopra:
        # # poz = p2.decidi_se_usare_pozione(p1)
        # # se poz != None → p2.usa_pozione(poz)
        # danno2 = p2.attacca(p1)
        # print(f"{p2.nome} attacca {p1.nome} e infligge {danno2} danni!")
        # print(p1, "\n")


        # ------------------------------------------------------
        # FINE ROUND — SISTEMA BUFF (NUOVO Parte 3)
        # ------------------------------------------------------

        # # dopo che entrambi hanno giocato il turno, fai:
        # # p1.aggiorna_buff()
        # # p2.aggiorna_buff()
        # # (questo decrementa la durata e rimuove buff scaduti)

        turno += 1

    print("=== FINE COMBATTIMENTO ===\n")

    # ------------------------------------------------------
    # RISULTATO FINALE (lascialo identico)
    # ------------------------------------------------------

    if not p1.e_vivo() and not p2.e_vivo():
        print("Pareggio! Entrambi sono caduti in battaglia.")
    elif p1.e_vivo():
        print(f"🏆 {p1.nome} vince il combattimento! {p1}")
    else:
        print(f"🏆 {p2.nome} vince il combattimento! {p2}")
