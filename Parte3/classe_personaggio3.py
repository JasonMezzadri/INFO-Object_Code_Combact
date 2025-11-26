

from classe_arma3 import Arma
from classe_pozione3 import Pozione

class Personaggio:
    def __init__(self, nome: str, vita_massima: int, forza: int, destrezza: int):
        # --- Attributi privati originali (OK) ---
        self.__nome = nome
        self.__vita_massima = vita_massima
        self.__vita = vita_massima
        self.__forza = forza
        self.__destrezza = destrezza
        self.__arma = None

        # --- NUOVO Parte 3: buff e pozioni ---
        self.__buffs = []     # lista di (stat, bonus, durata)
        self.__pozioni = []   # max 3 pozioni

    # ===========================
    # PROPERTY nome (solo getter)
    # ===========================
    @property
    def nome(self):
        return self.__nome

    # ===========================
    # PROPERTY vita
    # ===========================
    @property
    def vita(self):
        return self.__vita

    @vita.setter
    def vita(self, valore):
        # # dopo aver impostato → chiama __limita_vita()
        pass

    @property
    def vita_massima(self):
        return self.__vita_massima

    # ===========================
    # PROPERTY forza
    # ===========================
    @property
    def forza(self):
        return self.__forza

    @forza.setter
    def forza(self, valore):
        # # valida range 1–20
        pass

    # ===========================
    # PROPERTY destrezza
    # ===========================
    @property
    def destrezza(self):
        return self.__destrezza

    @destrezza.setter
    def destrezza(self, valore):
        # # valida range 1–20
        pass

    # ===========================
    # PROPERTY arma
    # ===========================
    @property
    def arma(self):
        return self.__arma

    @arma.setter
    def arma(self, valore):
        # # deve essere None oppure Arma
        pass

    # ===========================
    # NUOVE PROPERTY Parte 3
    # ===========================
    @property
    def forza_effettiva(self):
        # # somma forza + buff_forza
        pass

    @property
    def destrezza_effettiva(self):
        # # somma destrezza + buff_destrezza
        pass

    @property
    def pozioni(self):
        return self.__pozioni

    @pozioni.setter
    def pozioni(self, lista):
        # # verifica che siano tutte Pozione
        # # max 3
        pass

    # ===========================
    # METODI ORIGINALI CHE VANNO BENE
    # ===========================
    def e_vivo(self) -> bool:
        return self.__vita > 0    # <--- QUESTO LASCIALO COSÌ!

    def __modificatore(self, valore: int) -> int:
        return (valore - 10) // 2  # <--- anche questo rimane

    # ===========================
    # METODI NUOVI Parte 3
    # ===========================
    def cura(self, quantita: int):
        # # aumenta la vita e poi applica clamp
        pass

    def aggiungi_buff(self, stat, valore, durata):
        # # append alla lista __buffs
        pass

    def aggiorna_buff(self):
        # # decrementa durata buff e rimuovi quelli finiti
        pass

    # ===========================
    # ATTACCO — DA AGGIORNARE
    # ===========================
    def attacca(self, nemico: "Personaggio"):
        # # ora devi usare __calcola_danno() al posto di farlo qui
        pass

    # ===========================
    # POZIONI
    # ===========================
    def usa_pozione(self, pozione):
        # # chiama pozione.applica_a(self)
        # # rimuovi dall’inventario
        pass

    def decidi_se_usare_pozione(self, nemico):
        # # qui metti la tua logica autonoma
        pass

    # ===========================
    # METODI PRIVATI NUOVI
    # ===========================
    def __calcola_danno(self):
        # # prendi danno arma
        # # aggiungi modificatore FORZA o DESTREZZA *effettivi*
        pass

    def __subisci(self, danno):
        # # come tua funzione subisci, ma ora deve essere privata
        pass

    def __limita_vita(self):
        # # clamp tra 0 e vita_massima
        pass

    # ===========================
    # STAMPA (TIENILA)
    # ===========================
    def __str__(self):
        return f"{self.__nome} (HP: {self.__vita}/{self.__vita_massima})"
