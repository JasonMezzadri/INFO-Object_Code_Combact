class Pozione:
    def __init__(self, nome: str, effetto: str, quantita: int, durata: int = 0):
        if nome == "":
            raise ValueError("Il nome della pozione non può essere vuoto")
        if effetto not in ["cura", "buff_forza", "buff_destrezza"]:
            raise ValueError("Effetto della pozione non ammesso")
        if quantita < 1:
            raise ValueError("La quantità deve essere >= 1")
        if durata < 0:
            raise ValueError("La durata non può essere negativa")

        self.__nome = nome
        self.__effetto = effetto
        self.__quantita = quantita
        self.__durata = durata
        self.__consumata = False

    @property
    def nome(self):
        return self.__nome

    @property
    def effetto(self):
        return self.__effetto

    @property
    def quantita(self):
        return self.__quantita

    @property
    def durata(self):
        return self.__durata

    def applica_a(self, target):
        # Cura
        if self.__effetto == "cura":
            if target.vita == target.vita_massima:
                raise ValueError("Impossibile usare la pozione: HP già massimi")
            target.heal(self.__quantita)
            return {"effetto": "cura", "quantita": self.__quantita}

        # Buff forza
        if self.__effetto == "buff_forza":
            if target.ha_buff("forza"):
                raise ValueError("Buff alla forza già attivo")
            target.aggiungi_buff("forza", self.__quantita, self.__durata)
            return {"effetto": self.__effetto, "quantita": self.__quantita, "durata": self.__durata}

        # Buff destrezza
        if self.__effetto == "buff_destrezza":
            if target.ha_buff("destrezza"):
                raise ValueError("Buff alla destrezza già attivo")
            target.aggiungi_buff("destrezza", self.__quantita, self.__durata)
            return {"effetto": self.__effetto, "quantita": self.__quantita, "durata": self.__durata}

        raise ValueError("Tipo di pozione non riconosciuto")

    def __str__(self):
        return f"{self.__nome}: Effetto={self.__effetto}, Quantità={self.__quantita}, Durata={self.__durata}"

