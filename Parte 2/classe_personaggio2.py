from classe_arma2 import Arma

class Personaggio:
    def __init__(self, nome: str, vita_massima: int, forza: int, destrezza: int):
        # Attributi privati
        self.__nome = nome
        self.__vita_massima = vita_massima
        self.__vita = vita_massima
        self.__forza = forza
        self.__destrezza = destrezza
        self.__arma = None

    # Getter e Setter
    def get_nome(self):
        return self.__nome

    def get_vita(self):
        return self.__vita

    def get_vita_massima(self):
        return self.__vita_massima

    def get_forza(self):
        return self.__forza

    def get_destrezza(self):
        return self.__destrezza

    def get_arma(self):
        return self.__arma

    def set_vita(self, valore: int):
        self.__vita = max(0, min(valore, self.__vita_massima))

    def set_arma(self, arma: Arma):
        self.__arma = arma

    # Equipaggia un'arma
    def equipaggia(self, arma: Arma):
        self.__arma = arma

    # Calcola modificatore
    def __modificatore(self, valore: int) -> int:
        return (valore - 10) // 2

    # Verifica se è vivo
    def e_vivo(self) -> bool:
        return self.__vita > 0

    # Subisce danno
    def subisci(self, danno: int) -> int:
        danno_effettivo = max(0, danno)
        self.__vita = max(0, self.__vita - danno_effettivo)
        return danno_effettivo

    # Attacca un nemico
    def attacca(self, nemico: "Personaggio") -> int:
        if not self.__arma:
            danno = 1
        else:
            danno = self.__arma.get_danno()
            if self.__arma.get_tipo() == "mischia":
                danno += self.__modificatore(self.__forza)
            else:
                danno += self.__modificatore(self.__destrezza)
        danno = max(0, danno)
        return nemico.subisci(danno)

    def __str__(self):
        return f"{self.__nome} (HP: {self.__vita}/{self.__vita_massima})"