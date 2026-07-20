class Pessoa:
    def __init__(self, nome = '', idade = 0, profissao = ''):
        self.nome = nome.title()
        self.idade = idade
        self.profissao = profissao.title()
        
    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.profissao}'
    
    def aniversario(self):
        self.idade += 1
    
    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá {self.profissao} {self.nome}, você têm {self.idade} anos'
        else:
            return f'Olá, sou {self.nome}'

Thiago = Pessoa(nome = 'Thiago', idade = 23, profissao = 'Dev')
print(Thiago.saudacao)