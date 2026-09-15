from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tipo):
        super().__init__(nome,preco)
        self.tipo = tipo

    def __str__(self):
        return self._nome