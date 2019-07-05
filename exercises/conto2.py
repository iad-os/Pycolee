# Testo dell'esercizio
# Definire una classe ContoCorrente sottoclasse di Object.
# Definire il costruttore di ContoCorrente che accetta
# in input 3 parametri: nome, conto e importo. Gli attributi
# di istanza sono nome, conto e saldo.
# Definire il saldo come attributo nascosto.
# Definire una property getter, di nome saldo, che ritorna
# il saldo.
# Definire una property setter, di nome saldo, che modifica
# l'attributo saldo.
# All'interno del metodo setter chiamare il metodo che sottrae
# il saldo portandolo a zero. Chiamare poi il metodo deposita
# che definisce il nuovo importo pari al saldo.
# Definire un metodo preleva che accetta in input un importo
# che preleverà dal saldo una certa somma ogni volta che verrà
# invocato.
# Definire un metodo deposita che accetta in unput un importo
# che aggiungerà una certa somma ogni volta che verrà
# invocato.
# Definire un metodo descrizione che stampa il nome del titolare,
# il numero del conto e il saldo.


class ContoCorrente:
    def __init__(self, nome, conto, importo):
        self.nome = nome
        self.conto = conto
        self.__saldo = importo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, importo):
        self.preleva(self.__saldo)
        self.deposita(importo)

    def preleva(self, importo):
        self.__saldo -= importo

    def deposita(self, importo):
        self.__saldo += importo

    def descrizione(self):
        print('Nome titolare: ' +
              self.nome +
              ', conto corrente: ' +
              self.conto +
              ', saldo: ' +
              str(self.__saldo))


conto_corrente1 = ContoCorrente('Marco Orfei', '000123456', 1000)
conto_corrente2 = ContoCorrente('Pietro Ciaco', '100123456', 500)

conto_corrente1.descrizione()
conto_corrente2.descrizione()

print('Definite le property invoco' +
      'il setter saldo e stampo i nuovi conti corrente')
conto_corrente1.saldo = 5000
conto_corrente2.saldo = 3000

conto_corrente1.descrizione()
conto_corrente2.descrizione()
