from modelos.restaurante_novo import Restaurante

restaurante1 = Restaurante('MilkMu', 'Sorveteria')
restaurante2 = Restaurante('Bruscheta da Nona', 'Cantina Italiana')
restaurante3 = Restaurante('Hayumi Sushi', 'Comida Japonesa')
def main():
    Restaurante.listar_restaurantes()
if __name__ == '__main__':
    main()