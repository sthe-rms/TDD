from app.cliente import Cliente
from app.sistema_pontuacao import SistemaPontuacao


def test_calcular_pontos_compra_cliente_padrao():
    cliente_padrao = Cliente(nome="Sthe", tipo="padrao")
    sistema = SistemaPontuacao()
    valor_compra = 100.00
    pontos_esperados = 100

    pontos_calculados = sistema.calcular_pontos(cliente_padrao, valor_compra)

    assert pontos_esperados == pontos_calculados

def test_calcular_pontos_cliente_premium():
    cliente_premium = Cliente(nome="Paulo", tipo="premium")
    sistema = SistemaPontuacao()
    valor_compra = 100.00
    pontos_esperados = 150

    pontos_calculados = sistema.calcular_pontos(cliente_premium, valor_compra)

    assert pontos_esperados == pontos_calculados

def test_calcular_pontos_cliente_vip():
    cliente_vip = Cliente(nome="Ana", tipo="vip")
    sistema = SistemaPontuacao()
    valor_compra = 100.00
    pontos_esperados = 200

    pontos_calculados = sistema.calcular_pontos(cliente_vip, valor_compra)

    assert pontos_esperados == pontos_calculados

def test_acumular_pontos_varias_compras():
    cliente = Cliente(nome="Lucas", tipo="premium")
    sistema = SistemaPontuacao()

    compras = [100.00, 100.00]
    pontos_esperados = 300

    for compra in compras:
        sistema.atualizar_pontos_cliente(cliente, compra)
        pontos_esperados += sistema.calcular_pontos(cliente, compra)

    assert cliente.pontos == pontos_esperados