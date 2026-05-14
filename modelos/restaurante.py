#Classe = Define um conjunto de caracteristicas que objetos pertencentes a ela têm em comum
class restaurante:
    def __init__(self,nome,categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
#Criação de Objeto
restaurante_muhaui = restaurante('Muhaui', 'Vegano')
#Atributo de instancia
print(vars(restaurante_muhaui ))