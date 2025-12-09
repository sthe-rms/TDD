class Cliente:
    def __init__(self, nome,tipo, pontos):
        self.nome = nome
        self.tipo = tipo
        self.pontos = pontos

    def __repr__(self):
        return f"Cliente(nome={self.nome}, tipo={self.tipo}, pontos={self.pontos})"
