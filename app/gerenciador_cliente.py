from .cliente import Cliente

class GerenciadorCliente:
    def __init__(self):
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def buscar_cliente_por_nome(self, nome: str):
        for cliente in self.clientes:
            if cliente.nome == nome:
                return cliente
        
        raise ValueError("Cliente inexistente")
    
    #metodo para filtra os cliente com pontos acima do limite
    def filtrar_clientes_com_pontos_acima_de_limite(self, limite):
        return [cliente for cliente in self.clientes if cliente.pontos > limite]
    
    # metodo ordenar cliente 
    def ordenar_clientes_por_pontos(self):
        return sorted(self.clientes, key = lambda cliente: cliente.pontos, reverse = True)
    
    #metodo para remover cliente com saldo zero
    def remover_clientes_com_saldo_zero(self):
        self.clientes = [cliente for cliente in self.clientes if cliente.pontos != 0]

    #metodo para somar todosos posntos da lista

    def somar_total_pontos_lista(self):
        return sum(clientes.pontos for clientes in self.clientes)
    
    #Metodo para organizar ranking na ordem decrescente

    def ranking_clientes_por_pontos(self):
        return sorted(self.clientes, key=lambda cliente: cliente.pontos, reverse  = True)
    
    
                                
    
    
        
   