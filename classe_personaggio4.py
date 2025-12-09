from classe_arma4 import Arma
from classe_pozione4 import Pozione

class Personaggio:
    def __init__(self, nome: str, vita_massima: int, forza: int, destrezza: int):
        if not isinstance(vita_massima, int) or vita_massima <= 0:
            raise ValueError("La vita massima deve essere > 0")
        if not isinstance(forza, int) or forza <= 0:
            raise ValueError("La forza deve essere > 0")
        if not isinstance(destrezza, int) or destrezza <= 0:
            raise ValueError("La destrezza deve essere > 0")

        self.__nome = nome
        self.__vita_massima = vita_massima
        self.__vita = vita_massima
        self.__forza = forza
        self.__destrezza = destrezza
        self.__arma = None
        self.__buffs = []
        self.__pozioni = []

    # PROPERTY
    @property
    def nome(self):
        return self.__nome

    @property
    def vita(self):
        return self.__vita

    @property
    def vita_massima(self):
        return self.__vita_massima

    @property
    def forza(self):
        return self.__forza

    @property
    def destrezza(self):
        return self.__destrezza

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
    def arma(self):
        return self.__arma

    def equip(self, nuova_arma):
        if not hasattr(nuova_arma, "get_danno") or not hasattr(nuova_arma, "tipo"):
            raise TypeError("Oggetto non equipaggiabile: non è un'Arma valida")
        self.__arma = nuova_arma

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

    # METODI
    def e_vivo(self):
        return self.__vita > 0

    def take_damage(self, amount: int):
        if not isinstance(amount, int):
            raise TypeError("Il danno deve essere un intero")
        if amount < 0:
            raise ValueError("Non puoi subire danno negativo")
        self.__vita -= amount
        if self.__vita < 0:
            self.__vita = 0

    def heal(self, amount: int):
        if not isinstance(amount, int):
            raise TypeError("La cura deve essere un intero")
        if amount < 0:
            raise ValueError("La cura non può essere negativa")
        self.__vita += amount
        if self.__vita > self.__vita_massima:
            self.__vita = self.__vita_massima

    def applica_cura(self, quantita: int):
        self.heal(quantita)

    def aggiungi_buff(self, stat, valore, durata):
        self.__buffs.append((stat, valore, durata))

    def ha_buff(self, stat):
        for s, bonus, dur in self.__buffs:
            if s == stat:
                return True
        return False

    def aggiorna_buff(self):
        nuovi = []
        for stat, bonus, durata in self.__buffs:
            if durata > 1:
                nuovi.append((stat, bonus, durata - 1))
        self.__buffs = nuovi

    def attacca(self, nemico: "Personaggio"):
        danno = self.__calcola_danno()
        nemico.take_damage(danno)
        return danno

    def usa_pozione(self, pozione):
        if pozione not in self.__pozioni:
            return {"errore": "non_possiedi_questa_pozione"}
        log = pozione.applica_a(self)
        self.__pozioni.remove(pozione)
        return log

    def decidi_se_usare_pozione(self, nemico):
        if self.__vita < self.__vita_massima * 0.30:
            for p in self.__pozioni:
                if p.effetto == "cura":
                    return p
        if len(self.__buffs) == 0:
            for p in self.__pozioni:
                if p.effetto in ["buff_forza", "buff_destrezza"]:
                    return p
        return None

    def __calcola_danno(self):
        if self.__arma is None:
            danno_base = 1
        else:
            danno_base = self.__arma.get_danno()
        if self.__arma and self.__arma.tipo == "mischia":
            mod = (self.forza_effettiva - 10) // 2
        else:
            mod = (self.destrezza_effettiva - 10) // 2
        return max(1, danno_base + mod)

    def __str__(self):
        return f"{self.__nome} (HP: {self.__vita}/{self.__vita_massima})"
