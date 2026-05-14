#Classe = Define um conjunto de caracteristicas que selfs pertencentes a ela têm em comum
class Restaurante:
    restaurantes = []
    def __init__(self,nome,categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    
    #transformação de espaços de memória em string
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

#Criação de self
restaurante_muhaui = Restaurante('Muhaui', 'Vegano')
restaurante_oviedo = Restaurante('Oviedo', 'Ibérico')
#Atributo de instancia
Restaurante.listar_restaurantes()
