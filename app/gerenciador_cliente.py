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
    
    
        