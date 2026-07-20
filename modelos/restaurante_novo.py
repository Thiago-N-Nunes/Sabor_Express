#Criação de classe
class Restaurante:
    restaurantes = [] #Essa lista vai receber todos os restaurantes que forem cadastrados

    def __init__(self,nome, categoria):#Cria um 'Criador' - uma cadeia de caracteristicas que será tratado como obrigatória para os objetos da classe 
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self) # Toda vez que um restaurante for criado, será armazenado na lista 'restaurantes'
        
#    def __str__(self): #Transforma a maneira de visualizar os objetos/atributos


    @classmethod #Método para a classe
    def listar_restaurantes(cls):# metodo que mostra os restaurantes
        print(f'{'RESTAURANTE'.ljust(25)} | {'CATEGORIA'.ljust(25)} | {'SITUAÇÃO'.ljust(25)}')
        for restaurante in cls.restaurantes: #Loop para percorrer a lista de restaurantes
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo.ljust(25)}')

    @property
    def ativo(self):
        return '✅' if self._ativo else '✖'
    def alternar_estado(self):#Método para os objetos da classe
        self._ativo = not self._ativo

restaurante_zuko = Restaurante('zuko sushi', 'Asiatico')
restaurante_zuko.alternar_estado()
restaurante_Torf = Restaurante('torf habib', 'Arabe')
     
Restaurante.listar_restaurantes()