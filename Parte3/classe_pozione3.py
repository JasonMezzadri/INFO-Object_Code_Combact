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


    def applica_a(self, bersaglio):
        """
        Applica l’effetto della pozione al bersaglio.
        Restituisce un dizionario di log, es:
        {"effetto": "cura", "quantita": 10, "durata": 0}
        """

        # # 2. verifica che il bersaglio abbia i metodi necessari
        # #    usa hasattr(bersaglio, 'cura') e callable(...)

        # # 3. usa l'effetto corretto:
        # #    - se cura → chiama __applica_cura(bersaglio)
        # #    - se buff_forza → chiama __applica_buff(bersaglio, "forza")
        # #    - se buff_destrezza → chiama __applica_buff(bersaglio, "destrezza")

        # # 4. imposta __consumata = True

        # # 5. ritorna un dizionario log con "effetto", "quantita", "durata"
        pass

    # ===========================
    # METODI PRIVATI
    # ===========================
    def __applica_cura(self, bersaglio):
        # # chiama bersaglio.cura(self.__quantita)
        # # restituisce la quantita curata (opzionale)
        pass

    def __applica_buff(self, bersaglio, statistica):
        # # chiama:
        # # bersaglio.aggiungi_buff(statistica, self.__quantita, self.__durata)
        pass

    # ===========================
    # STRINGA DI DESCRIZIONE
    # ===========================
    def __str__(self):
        # # se cura:
        # #   return f"Pozione(cura +{self.__quantita})"
        # #
        # # se buff:
        # #   return f"Pozione(buff {self.__effetto} +{self.__quantita} x{self.__durata}t)"
        pass
