#Classe = Define um conjunto de caracteristicas que selfs pertencentes a ela têm em comum
class Restaurante:
    restaurantes = []
    def __init__(self,nome,categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    #transformação de espaços de memória em string
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
#Criação de método 
    def listar_restaurantes():
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria do Restaurante'.ljust(25)} | {'Status do Restaurante'.ljust(25)}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo.ljust(25)}')
#Modificação de como o atributo é lido
    @property
    def ativo(self):
        return '✔️' if self._ativo else '✖️'

#Criação de self
restaurante_muhaui = Restaurante('Muhaui', 'Vegano')
restaurante_oviedo = Restaurante('Oviedo', 'Ibérico')
#Atributo de instancia
Restaurante.listar_restaurantes()
