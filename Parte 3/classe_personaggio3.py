from classe_arma3 import Arma
from classe_pozione3 import Pozione

class Personaggio:
    def __init__(self, nome: str, vita_massima: int, forza: int, destrezza: int):
        # --- Attributi privati ---
        self.__nome = nome
        self.__vita_massima = vita_massima

        self.__vita = vita_massima
        self.__forza = forza
        self.__destrezza = destrezza
        self.__arma = None

        # Parte 3
        self.__buffs = []     # lista di (stat, bonus, durata)
        self.__pozioni = []   # max 3


    # ===========================
    # PROPERTY nome
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

    @property
    def vita_massima(self):
        return self.__vita_massima


    # ===========================
    # PROPERTY forza/destrezza
    # ===========================
    @property
    def forza(self):
        return self.__forza

    @property
    def destrezza(self):
        return self.__destrezza


    # ===========================
    # PROPERTY arma (con setter)
    # ===========================
    @property
    def arma(self):
        return self.__arma

    @arma.setter
    def arma(self, nuova_arma):
        if nuova_arma is not None and not isinstance(nuova_arma, Arma):
            raise TypeError("L'arma deve essere None oppure un'istanza di Arma")
        self.__arma = nuova_arma


    # ===========================
    # PROPERTY Parte 3
    # ===========================
    @property
    def forza_effettiva(self):
        totale = self.__forza
        for stat, bonus, durata in self.__buffs:
            if stat == "forza":
                totale += bonus
        return totale

    @property
    def destrezza_effettiva(self):
        totale = self.__destrezza
        for stat, bonus, durata in self.__buffs:
            if stat == "destrezza":
                totale += bonus
        return totale


    @property
    def pozioni(self):
        return self.__pozioni

    @pozioni.setter
    def pozioni(self, lista):
        if len(lista) > 3:
            raise ValueError("Puoi avere al massimo 3 pozioni")

        for p in lista:
            if not isinstance(p, Pozione):
                raise TypeError("Tutti gli oggetti devono essere istanze di Pozione")

        self.__pozioni = lista


    # ===========================
    # METODI ORIGINALI
    # ===========================
    def e_vivo(self) -> bool:
        return self.__vita > 0

    def __modificatore(self, valore: int) -> int:
        return (valore - 10) // 2


    # ===========================
    # METODI PARTE 3
    # ===========================
    def applica_cura(self, quantita: int):
        self.__vita += quantita
        if self.__vita > self.__vita_massima:
            self.__vita = self.__vita_massima


    def aggiungi_buff(self, stat, valore, durata):
        # stat deve essere "forza" o "destrezza"
        self.__buffs.append((stat, valore, durata))


    def aggiorna_buff(self):
        nuovi = []
        for stat, bonus, durata in self.__buffs:
            if durata > 1:
                nuovi.append((stat, bonus, durata - 1))
        self.__buffs = nuovi


    # ===========================
    # ATTACCO
    # ===========================
    def attacca(self, nemico: "Personaggio"):
        danno = self.__calcola_danno()
        nemico.__subisci(danno)
        return danno


    # ===========================
    # POZIONI
    # ===========================
    def usa_pozione(self, pozione):
        if pozione not in self.__pozioni:
            return {"errore": "non_possiedi_questa_pozione"}

        log = pozione.applica_a(self)

        # rimuovi solo se applicata correttamente
        if "errore" not in log:
            self.__pozioni.remove(pozione)

        return log


    def decidi_se_usare_pozione(self, nemico):
        """
        Logica semplice:
        - Se vita sotto il 30% → prova a usare una pozione curativa
        - Altrimenti, se non hai buff attivi → usa un buff
        - Altrimenti niente
        """

        # 1) cura se vita bassa
        if self.__vita < self.__vita_massima * 0.30:
            for p in self.__pozioni:
                if p.effetto == "cura":
                    return p

        # 2) buff se nessun buff attivo
        if len(self.__buffs) == 0:
            for p in self.__pozioni:
                if p.effetto in ["potenzia_forza", "potenzia_destrezza"]:
                    return p

        return None  # non usare alcuna pozione


    # ===========================
    # METODI PRIVATI
    # ===========================
    def __calcola_danno(self):
        if self.__arma is None:
            danno_base = 1
        else:
            danno_base = self.__arma.get_danno()

        # se arma da mischia usa forza, altrimenti destrezza
        if self.__arma and self.__arma.tipo == "mischia":
            mod = self.__modificatore(self.forza_effettiva)
        else:
            mod = self.__modificatore(self.destrezza_effettiva)

        return max(1, danno_base + mod)


    def __subisci(self, danno):
        self.__vita -= danno
        self.__limita_vita()
        return danno


    def __limita_vita(self):
        if self.__vita < 0:
            self.__vita = 0
        if self.__vita > self.__vita_massima:
            self.__vita = self.__vita_massima


    # ===========================
    # STAMPA
    # ===========================
    def __str__(self):
        return f"{self.__nome} (HP: {self.__vita}/{self.__vita_massima})"
