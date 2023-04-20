from conta  import Conta


def inicio():
   contrato = criar_conta( 1234,"Leandro", 1000.0, 10000.0)

   contrato.extro()
   contrato.deposita(50.0)
   contrato.extro()
   contrato.sacar(2000.0)
   contrato.extro()


def criar_conta(titulo,numero,saldo,limite):
    conta = Conta(titulo,numero,saldo,limite)
    return conta

# def deposita(conta,valor):
#     conta.saldo += valor


# def saca(conta,valor):
#     conta.saldo -= valor



if __name__ == '__main__':
    inicio()
