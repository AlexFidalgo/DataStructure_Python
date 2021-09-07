class Produto:
    
    def __init__(self, nome, codigo, preco, quantidade):
        self._nome = nome
        self._codigo = codigo
        self._preco = preco
        self._quantidade = quantidade       
    def obtem_nome(self):
        return self._nome   
    def obtem_codigo(self):
        return self._codigo  
    def obtem_preco(self):
        return self._preco  
    def obtem_quantidade(self):
        return self._quantidade  
    def altera_preco(self, novo_preco):
        pp = self._preco
        self._preco = novo_preco
        if novo_preco > pp:
            return True
        return False 
    def altera_quantidade(self, novo_pedido):
        if novo_pedido > self._quantidade:
            return False
        self.quantidade = self._quantidade - novo_pedido
        return True
    
class ProdutoCritico(Produto):
    def __init__(self, nome, codigo, preco, quantidade, estoque_min):
        super().__init__(nome, codigo, preco, quantidade) #chama a __init__ da classe mae
        self._estoque_min = estoque_min
    def altera_quantidade(self, novo_pedido):
        if novo_pedido + self._estoque_min > self._quantidade:
            return False
        return super().altera_quantidade(novo_pedido)
    def altera_preco(self, novo_preco):
        pp = self._preco
        if novo_preco > 1.1*pp or novo_preco < 0.9*pp:
            return False
        ap = super().altera_preco(novo_preco)
        return True

pc1 = ProdutoCritico("Capitão Cueca", 3, 9.99, 10000, 100)
pc2 = ProdutoCritico("Laranja Mecanica", 4, 29.99, 100, 2)
print("Oferta do dia: ", pc1.obtem_nome())
print("Oferta da semana: ", pc2.obtem_nome())
if pc1.altera_preco(8):
    print("Preco alterado hoje")
else:
    print("diferença > 10% - Preço não alterado")
if pc1.altera_quantidade(800):
    print("Pode vender", pc2.obtem_preco()*800)
else:
    print("Não tem produto suficiente ou excedeu o estoque mínimo")
