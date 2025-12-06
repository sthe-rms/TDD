from app.cliente import Cliente
from app.sistema_pontuacao import SistemaPontuacao


def test_calcular_pontos_compra_cliente_padrao():
    cliente_padrao = Cliente(nome="Sthe", tipo="padrao")
    sistema = SistemaPontuacao()
    valor_compra = 150.00
    pontos_esperados = 150

    pontos_calculados = sistema.calcular_pontos(cliente_padrao, valor_compra)

    assert pontos_esperados == pontos_calculados