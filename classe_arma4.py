import random

class Arma:
    def __init__(self, nome: str, danno_minimo: int, danno_massimo: int, tipo: str):
        # Validazioni Parte 4
        if nome == "":
            raise ValueError("Il nome dell'arma non può essere vuoto")
        if not isinstance(danno_minimo, int) or not isinstance(danno_massimo, int):
            raise TypeError("Danno minimo e massimo devono essere interi")
        if danno_minimo < 1:
            raise ValueError("Il danno minimo deve essere >= 1")
        if danno_massimo < danno_minimo:
            raise ValueError("Il danno massimo non può essere minore del danno minimo")
        if tipo not in ["mischia", "distanza"]:
            raise ValueError("Il tipo deve essere 'mischia' o 'distanza'")

        self.__nome = nome
        self.__danno_minimo = danno_minimo
        self.__danno_massimo = danno_massimo
        self.__tipo = tipo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nuovo_nome):
        if nuovo_nome == "":
            raise ValueError("Il nome non può essere vuoto")
        self.__nome = nuovo_nome

    @property
    def danno_minimo(self):
        return self.__danno_minimo

    @danno_minimo.setter
    def danno_minimo(self, nuovo):
        if nuovo < 1:
            raise ValueError("Il danno minimo deve essere >= 1")
        self.__danno_minimo = nuovo

    @property
    def danno_massimo(self):
        return self.__danno_massimo

    @danno_massimo.setter
    def danno_massimo(self, nuovo):
        if nuovo < 1:
            raise ValueError("Il danno massimo deve essere >= 1")
        if nuovo < self.__danno_minimo:
            raise ValueError("Il danno massimo non può essere minore del danno minimo")
        self.__danno_massimo = nuovo

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valore):
        if valore not in ["mischia", "distanza"]:
            raise ValueError("Il tipo deve essere 'mischia' oppure 'distanza'")
        self.__tipo = valore

    def get_danno(self):
        return random.randint(self.__danno_minimo, self.__danno_massimo)

    def __str__(self):
        return f"{self.__nome} ({self.__danno_minimo}-{self.__danno_massimo} dmg, tipo: {self.__tipo})"
