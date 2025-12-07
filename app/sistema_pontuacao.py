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