import random

class Arma:
    def __init__(self, nome: str, danno_minimo: int, danno_massimo: int, tipo: str):
        # Attributi privati
        self.__nome = nome
        self.__danno_minimo = max(1, danno_minimo)
        self.__danno_massimo = max(self.__danno_minimo + 1, danno_massimo)
        self.__tipo = tipo if tipo in ["mischia", "distanza"] else "mischia"

    # Getter e Setter per ogni attributo
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome: str):
        if isinstance(nome, str) and nome:
            self.__nome = nome

    def get_danno_minimo(self):
        return self.__danno_minimo

    def set_danno_minimo(self, valore: int):
        if valore >= 1 and valore <= self.__danno_massimo:
            self.__danno_minimo = valore

    def get_danno_massimo(self):
        return self.__danno_massimo

    def set_danno_massimo(self, valore: int):
        if valore >= self.__danno_minimo:
            self.__danno_massimo = valore

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo: str):
        if tipo in ["mischia", "distanza"]:
            self.__tipo = tipo

    # Metodo per ottenere il danno casuale
    def get_danno(self) -> int:
        return random.randint(self.__danno_minimo, self.__danno_massimo)

    def __str__(self):
        return f"{self.__nome} ({self.__danno_minimo}–{self.__danno_massimo} dmg, tipo: {self.__tipo})"