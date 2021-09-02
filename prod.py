#O nome self refere-se ao particular objeto sendo criado. Note que o primeiro parâmetro é sempre self na
# definição. No uso ou na chamada do método esse primeiro parâmetro não existe

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

if __name__ == "__main__":
    
    p1 = Produto ("Palhaço", 1, 69.99, 300)
    p2 = Produto ("Ursinho", 2, 30.00, 5)
    
    print("Oferta do dia: ", p1.obtem_nome())
    print("Oferta da semana: ", p2.obtem_nome())
    
    if p1.altera_preco(59.99):
        print("Preço alterado hoje")
    else:
        print("Preço abaixou, criançada")
        
    if p2.altera_quantidade(3):
        print("Pode fazer a venda. Valor total = ", p2.obtem_preco()*3)
    else:
        print("Somente possuímos ", p2.obtem_quantidade())
