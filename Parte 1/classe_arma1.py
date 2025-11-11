import random

class Arma:
    def __init__(self, nome:str, danno_minimo:str, danno_massimo:str, tipo:str):
        self.nome = nome
        #Controllo dei limiti del danno (minimo e massimo)
        if danno_minimo >= 1:
            self.danno_minimo = danno_minimo
        else:
            print("Attenzione!! Il danno minimo non è maggiore/uguale ad 1.")
            self.danno_minimo = 1
        
        if danno_massimo >= danno_minimo:
            self.danno_massimo = danno_massimo
        else:
            print("Attenzione!! Il danno massimo è più piccolo della condizione.")
            self.danno_massimo = self.danno_minimo + 1

        #Controllo di che tipo di arma si tratta
        if tipo == "mischia" or tipo == "distanza":
            self.tipo = tipo
        else:
            print("ERRORE! Il tipo dev'essere mischia o distanza")
            self.tipo = "mischia" #Arma che viene inserita di default

    def get_danno(self) -> int:
        numero_casuale = random.randint(self.danno_minimo, self.danno_massimo)
        return numero_casuale
    
    def __str__(self):
        return f"Nome: {self.nome}, ({self.danno_minimo}, {self.danno_massimo}), Tipo: {self.tipo}"