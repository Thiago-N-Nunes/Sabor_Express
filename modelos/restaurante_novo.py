#Criação de classe
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False
    
restaurante_zuko = Restaurante()
restaurante_zuko.nome = 'Zuko Sushi'
restaurante_zuko.categoria = 'Asiatico'
restaurante_soka = Restaurante()

restaurantes = [restaurante_zuko, restaurante_soka]

print(restaurante_zuko.ativo)