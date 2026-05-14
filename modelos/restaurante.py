#Classe = Define um conjunto de caracteristicas que selfs pertencentes a ela têm em comum
class restaurante:
    def __init__(self,nome,categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

#Criação de self
restaurante_muhaui = restaurante('Muhaui', 'Vegano')
#Atributo de instancia
print(restaurante_muhaui)

