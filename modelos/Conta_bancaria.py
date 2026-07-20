class Conta_bancaria:
    contas = []
    def __init__(self,nome = '',saldo = 0):
        self._titular = nome.title()
        self._saldo = saldo
        self._ativo = False
        Conta_bancaria.contas.append(self)
    
    def __str__(self):
        return f'Titular: 👤 {self._titular} | Saldo: R${self._saldo} | Situação da conta: {self.ativo}'
    
    @classmethod
    def listar_contas(cls):
        print(f'{'NOME'} | {'SALDO'.ljust(25)} | {'SITUAÇÃO DA CONTA'.ljust(25)}')
        for conta in cls.contas:
            print(f'Titular: 👤 {conta._titular} | Saldo: R${conta._saldo} | Situação da conta: {conta.ativo.ljust(25)}')
    
    @property
    def ativo(self):
        return 'Ativa ✅' if self._ativo else 'Desativada ⭕'
    def ativar_conta(self):
        self._ativo = True
Cliente1 = Conta_bancaria(nome = 'Thiago', saldo = 3000)
Cliente1.ativar_conta()
Cliente1 = Conta_bancaria(nome = 'Giovanna', saldo = 5000)
Conta_bancaria.listar_contas()
