#Classe = Define um conjunto de caracteristicas que objetos pertencentes a ela têm em comum
class restaurante:
    nome = ''
    categoria = ''
    ativo = False
#Criação de Objeto
restaurante_muhaui = restaurante()
#Atributo de instancia
restaurante_muhaui.nome = 'Muhaui'
restaurante_muhaui.categoria = 'Vegano'
print(vars(restaurante_muhaui))