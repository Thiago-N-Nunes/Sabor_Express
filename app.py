from modelos.cardapio.restaurante_novo import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebidas import Bebida

restaurante_milkmu = Restaurante('MilkMu', 'Sorveteria')
milkshake_morango = Bebida('Milkshake de Morango', 25.5, 'Sorvete')
petit_gateou = Prato('Petit Gateou', 25, 'Petit Gateou com bola de sorvete de creme')
restaurante_milkmu.adicionar_bebida_cardapio(milkshake_morango)
restaurante_milkmu.adicionar_prato_cardapio(petit_gateou)

def main():
    print(milkshake_morango)
    print(petit_gateou)

if __name__ == '__main__':
    main()