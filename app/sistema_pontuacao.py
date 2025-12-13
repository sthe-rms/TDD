from .cliente import Cliente

class SistemaPontuacao:
    def calcular_pontos(self, cliente: Cliente, valor_compra: float) -> float:
        if cliente.tipo == "padrao":
            return valor_compra * 1.0
        elif cliente.tipo == "premium":
            return valor_compra * 1.5
        elif cliente.tipo == "vip":
            return valor_compra * 2.0
        
        return 0.0
    
    def atualizar_pontos_cliente(self, cliente: Cliente, valor_compra: float) -> float:
        pontos_ganhos = self.calcular_pontos(cliente, valor_compra)
        cliente.pontos += pontos_ganhos

        return pontos_ganhos
    
    def consultar_pontos(self, cliente: Cliente) -> float:
        return cliente.pontos
    
    def resgatar_pontos(self, cliente: Cliente, pontos_resgatar: float) -> float:
        if pontos_resgatar > cliente.pontos:
            raise ValueError("Saldo insuficiente para o resgate.")
        
        cliente.pontos -= pontos_resgatar
        valor_desconto = pontos_resgatar * 0.05
        return valor_desconto
    
    def pontos_negativos(self, cliente: Cliente, pontos_resgatar: float) -> None:
        if pontos_resgatar < 0:
            raise ValueError("O valor de pontos para resgate deve ser positivo.")
        
    def quantidade_pontos_minima(self, cliente: Cliente) -> float:
        if cliente.pontos < 0:
            raise ValueError("O saldo de pontos não pode ser negativo.")

    def calcular_pontos_com_bonus(self, cliente: Cliente, valor_compra: float, bonus: float) -> float:
        pontos_base = self.calcular_pontos(cliente, valor_compra)
        pontos_totais = pontos_base + (pontos_base * bonus)
        return pontos_totais
    
    def expirar_pontos(self, cliente: Cliente, meses: int) -> None:
        if meses >= 12:
            cliente.pontos = 0 

    # metodo para calcular pontos da lista de clientes
    def calcular_pontos_lista_clientes(self, clientes, valor_compra):
        for cliente in clientes:
            self.atualizar_pontos_cliente(cliente, valor_compra)

    # metodo pra verificar se os pontos esta expirados
    def expirar_pontos(self, cliente, meses):
        if meses >= 2:
            cliente.pontos = 0
        elif meses >= 1:
            cliente.pontos *= 0.9
