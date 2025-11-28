class Pozione:
    def __init__(self, nome: str, effetto: str, quantita: int, durata: int = 0):
        
        if nome == "":
            raise ValueError("Il nome non può essere vuoto")

        if effetto not in ["cura", "potenzia_forza", "potenzia_destrezza"]:
            raise ValueError("Valore dell'effetto non ammesso")
        
        if quantita < 1:
            raise ValueError("La quantità non può essere < 1")
        
        if durata < 0:
            raise ValueError("La durata non può essere < 0")
        
        
        self.__nome = nome
        self.__effetto = effetto 
        self.__quantita = quantita
        self.__durata = durata
        self.__consumata = False


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nuovo_nome):
        if nuovo_nome == "":
            raise ValueError("Il nome non può essere vuoto")
        else:
            self.__nome = nuovo_nome
        

    @property
    def effetto(self):
        return self.__effetto

    @property
    def quantita(self):
        return self.__quantita

    @property
    def durata(self):
        return self.__durata


    def applica_a(self, giocatore):
        """
        Applica l’effetto della pozione al bersaglio.
        Restituisce un dizionario di log, es:
        {"effetto": "cura", "quantita": 10, "durata": 0}
        """
        if self.__effetto == 'cura':
            if hasattr(giocatore, 'applica_cura') and callable(getattr(giocatore, 'applica_cura')):
                giocatore.applica_cura(self.quantita)
                self.__consumata = True
            else:
                ValueError("L'attributo 'applica_cura' non è definito")
        else:
            if hasattr(giocatore, 'applica_buff') and callable(getattr(giocatore, 'applica_buff')):
                giocatore.applica_buff(self.quantita)
                self.__consumata = True
            else:
                ValueError("L'attributo 'applica_cura' non è definito")

        
    def __str__(self):
        return f"{self.__nome}: Effetto --> {self.__effetto}, Quantità --> {self.__quantita}, Durata --> {self.__durata}."
