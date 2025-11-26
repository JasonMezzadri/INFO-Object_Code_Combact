import random

class Arma:
    def __init__(self, nome: str, danno_minimo: int, danno_massimo: int, tipo: str):
        # # QUI devi usare i setter (property) invece di assegnare direttamente
        self.nome = nome
        self.danno_minimo = danno_minimo
        self.danno_massimo = danno_massimo
        self.tipo = tipo

    # ===========================
    # PROPERTY nome
    # ===========================
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valore):
        # # valida che non sia vuoto
        # # altrimenti mantieni il nome precedente
        pass

    # ===========================
    # PROPERTY danno_minimo
    # ===========================
    @property
    def danno_minimo(self):
        return self.__danno_minimo

    @danno_minimo.setter
    def danno_minimo(self, valore):
        # # valida che sia >= 1
        # # valida che non superi danno_massimo (se già definito)
        pass

    # ===========================
    # PROPERTY danno_massimo
    # ===========================
    @property
    def danno_massimo(self):
        return self.__danno_massimo

    @danno_massimo.setter
    def danno_massimo(self, valore):
        # # valida che sia >= danno_minimo
        pass

    # ===========================
    # PROPERTY tipo
    # ===========================
    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valore):
        # # accetta solo "mischia" o "distanza"
        pass

    # ===========================
    # IMMUATO: questo va bene
    # ===========================
    def get_danno(self) -> int:
        return random.randint(self.__danno_minimo, self.__danno_massimo)

    def __str__(self):
        return f"{self.__nome} ({self.__danno_minimo}–{self.__danno_massimo} dmg, tipo: {self.__tipo})"
