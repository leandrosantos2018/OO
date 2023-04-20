class Conta:

    def __init__(self,numero,titular,saldo,limite):
        print('construido objeto{}'.format(self))
        self.numero= numero,
        self.titulo = titular
        self.saldo = saldo
        self.limite = limite

    def extro(self):
        print("saldo é : {} e Titular é {}".format(self.saldo,self.titulo))

    def deposita(self,valor):
        self.saldo += valor

    def sacar(self,valor):
        if self.saldo <= valor:
            self.saldo -= valor


