from modelos.cardapio.restaurante_novo import Restaurante
from modelos.cardapio.sobremesa import Sobremesa
from modelos.cardapio.bebidas import Bebida

restaurante_milkmu = Restaurante('MilkMu', 'Sorveteria')
milkshake_morango = Bebida('Milkshake de Morango', 25.5, 'Sorvete')
petit_gateou = Sobremesa('Petit Gateou', 25, 'Sobremesa', 'Pequeno', 'Petit Gateou com bola de sorvete de creme')
restaurante_milkmu.adicionar_no_cardapio(milkshake_morango)
restaurante_milkmu.adicionar_no_cardapio(petit_gateou)

def main():
    restaurante_milkmu.exibir_cardapio


if __name__ == '__main__':
    main()