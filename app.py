from modelos.restaurante_novo import Restaurante

restaurante1 = Restaurante('MilkMu', 'Sorveteria')
restaurante2 = Restaurante('Bruscheta da Nona', 'Cantina Italiana')
restaurante3 = Restaurante('Hayumi Sushi', 'Comida Japonesa')
restaurante3.receber_avaliacao('Thiago', 10)
restaurante3.receber_avaliacao('Cauã', 5)
restaurante3.receber_avaliacao('Giovanna', 8)

def main():
    Restaurante.listar_restaurantes()
if __name__ == '__main__':
    main()