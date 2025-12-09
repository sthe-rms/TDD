from app.cliente import Cliente
from app.sistema_pontuacao import SistemaPontuacao
import pytest


def test_calcular_pontos_compra_cliente_padrao():
    cliente_padrao = Cliente(nome="Sthe", tipo="padrao", pontos=0)
    sistema = SistemaPontuacao()
    valor_compra = 100.00
    pontos_esperados = 100

    pontos_calculados = sistema.calcular_pontos(cliente_padrao, valor_compra)

    assert pontos_esperados == pontos_calculados

def test_calcular_pontos_cliente_premium():
    cliente_premium = Cliente(nome="Paulo", tipo="premium", pontos = 0)
    sistema = SistemaPontuacao()
    valor_compra = 100.00
    pontos_esperados = 150

    pontos_calculados = sistema.calcular_pontos(cliente_premium, valor_compra)

    assert pontos_esperados == pontos_calculados

def test_calcular_pontos_cliente_vip():
    cliente_vip = Cliente(nome="Ana", tipo="vip", pontos=0)
    sistema = SistemaPontuacao()
    valor_compra = 100.00
    pontos_esperados = 200

    pontos_calculados = sistema.calcular_pontos(cliente_vip, valor_compra)

    assert pontos_esperados == pontos_calculados

def test_acumular_pontos_varias_compras():
    cliente = Cliente(nome="Lucas", tipo="padrão", pontos=0)
    sistema = SistemaPontuacao()

    compras = [100.00, 100.00]
    pontos_esperados = 0.0

    for valor_compra in compras:
        sistema.atualizar_pontos_cliente(cliente, valor_compra)
        pontos_esperados += sistema.calcular_pontos(cliente, valor_compra)

    assert cliente.pontos == pontos_esperados

def test_consultar_pontos_cliente_existente():
    cliente = Cliente(nome="Mariana", tipo="vip", pontos=0)
    sistema = SistemaPontuacao()

    compras = [200.00, 150.00]
    pontos_esperados = 0.0

    for valor_compra in compras:
        sistema.atualizar_pontos_cliente(cliente, valor_compra)
        pontos_esperados += sistema.calcular_pontos(cliente, valor_compra)

    pontos_consultados = sistema.consultar_pontos(cliente)

    assert pontos_consultados == pontos_esperados

def test_resgatar_pontos_para_desconto():
    cliente = Cliente(nome="Carla", tipo="premium", pontos=5000)
    sistema = SistemaPontuacao()

    resgatePontos = 3000
    desconto_esperado = 150.0

    desconto_obtido = sistema.resgatar_pontos(cliente, resgatePontos)
    
    assert desconto_esperado == desconto_obtido
    assert cliente.pontos == 2000

def test_impedir_resgate_com_saldo_insuficiente():
    cliente = Cliente(nome="Paulo", tipo="padrao", pontos=1000)
    sistema = SistemaPontuacao()

    resgatePontos = 1500

    with pytest.raises(ValueError) as excinfo:
        sistema.resgatar_pontos(cliente, resgatePontos)

    assert str(excinfo.value) == "Saldo insuficiente para o resgate."

def test_resgatar_todos_os_pontos_disponiveis():
    cliente = Cliente(nome="Fernanda", tipo="vip", pontos=2500)
    sistema = SistemaPontuacao()

    resgatePontos = 2500
    desconto_esperado = 125.0

    desconto_obtido = sistema.resgatar_pontos(cliente, resgatePontos)

    assert desconto_esperado == desconto_obtido
    assert cliente.pontos == 0

def test_nao_gerar_pontos_para_valor_zero():
    cliente = Cliente(nome="Rafael", tipo="premium", pontos=0)
    sistema = SistemaPontuacao()
    valor_compra = 0.00
    pontos_esperados = 0

    pontos_calculados = sistema.calcular_pontos(cliente, valor_compra)

    assert pontos_esperados == pontos_calculados

def test_gerar_pontos_para_valores_decimais():
    cliente = Cliente(nome="Bianca", tipo="padrao", pontos=0)
    sistema = SistemaPontuacao()
    valor_compra = 99.01
    pontos_esperados = 99.01
    pontos_calculados = sistema.calcular_pontos(cliente, valor_compra)

    assert pontos_esperados == pontos_calculados




