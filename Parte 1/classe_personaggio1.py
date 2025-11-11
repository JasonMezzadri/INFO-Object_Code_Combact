from classe_arma1 import Arma

class Personaggio:
    def __init__(self, nome:str, vita_massima:int, forza:int, destrezza:int):
        self.nome = nome
        self.vita_massima = vita_massima
        self.vita = self.vita_massima
        self.forza = forza 
        self.destrezza = destrezza
        self.arma = None

    #Funzione che assegna un'arma al personaggio
    def equipaggia(self, arma: Arma):
        self.arma = arma

    #Funzione che calcola il modifcatore 
    def modificatore(self, valore: int):
        return ((valore - 10) // 2)
    
    #Funzione che controlla se il personaggio è ancora vivo
    def e_vivo(self) -> bool:
        if self.vita > 0:
            return True
        else:
            return False
        
    #Funzione che riduce la vita del personaggio
    def subisci(self, danno: int) -> int:
        danno_effettivo = max(0, danno)
        self.vita = max(0, self.vita - danno_effettivo)
        return danno_effettivo
    
    #Funzione che gestisce l'attacco di un personaggio verso un altro
    def attacca(self, nemico: "Personaggio") -> int:
        #Se non ha un’arma equipaggiata, danno base = 1
        if not self.arma:
            danno = 1
        else:
            #Danno casuale dell’arma
            danno = self.arma.get_danno()
            #Aggiunge modificatore di forza o destrezza in base al tipo
            if self.arma.tipo == "mischia":
                danno += self.modificatore(self.forza)
            else: 
                danno += self.modificatore(self.destrezza)
        danno = max(0, danno)
        
        #Applica il danno al nemico
        return nemico.subisci(danno)
    
    def __str__(self):
        return f"{self.nome}: {self.vita}/{self.vita_massima} HP"