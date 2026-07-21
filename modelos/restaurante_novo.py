#importação de classe
from modelos.avaliacao import Avaliacao
#Criação de classe
class Restaurante:
    restaurantes = [] #Essa lista vai receber todos os restaurantes que forem cadastrados

    def __init__(self,nome, categoria):#Cria um 'Criador' - uma cadeia de caracteristicas que será tratado como obrigatória para os objetos da classe 
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []#Essa lista vai receber todos as avaliações que forem adicionadas
        Restaurante.restaurantes.append(self) # Toda vez que um restaurante for criado, será armazenado na lista 'restaurantes'
        
#    def __str__(self): #Transforma a maneira de visualizar os objetos/atributos


    @classmethod #Método para a classe
    def listar_restaurantes(cls):# metodo que mostra os restaurantes
        print(f'{'RESTAURANTE'.ljust(20)} | {'CATEGORIA'.ljust(20)} | {'AVALIAÇÃO'.ljust(20)} |{'SITUAÇÃO'.ljust(20)}')
        for restaurante in cls.restaurantes: #Loop para percorrer a lista de restaurantes
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacao).ljust(20)} | {restaurante.ativo.ljust(20)}')

    @property
    def ativo(self):
        return '✅' if self._ativo else '✖'
    
    def alternar_estado(self):#Método para os objetos da classe
        self._ativo = not self._ativo
    
    def receber_avaliacao(self,cliente,nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return '-'
        #sum(avaliacao._nota for avaliacao in self._avaliacao) = pega apenas as notas da classe avaliação e soma
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)  
        qtd_notas = len(self._avaliacao)
        media = round(soma_notas / qtd_notas,1)
        return media