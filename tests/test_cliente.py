from app.cliente import Cliente
from app.sistema_pontuacao import SistemaPontuacao
from app.gerenciador_cliente import GerenciadorCliente
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

def test_nao_permitir_pontos_negativos():
    cliente = Cliente(nome="Gustavo", tipo="vip", pontos = 0)
    sistema = SistemaPontuacao()

    cliente.pontos = -1
    saldo_negativo_esperado = -1

    with pytest.raises(ValueError) as excinfo:
        sistema.quantidade_pontos_minima(cliente)
    
    assert cliente.pontos == saldo_negativo_esperado

    assert str(excinfo.value) == "O saldo de pontos não pode ser negativo."

def test_cliente_inexsitente_lanca_excecao():
    gerenciador = GerenciadorCliente()

    with pytest.raises(ValueError, match="Cliente inexistente"):
        gerenciador.buscar_cliente_por_nome("Astrogildo")

def test_registrar_novo_cliente_com_pontos_iniciais():
    gerenciador = GerenciadorCliente()
    cliente_novo = Cliente(nome="Beatriz", tipo="padrao", pontos=50)

    gerenciador.adicionar_cliente(cliente_novo)
    cliente_registrado = gerenciador.buscar_cliente_por_nome("Beatriz")

    assert cliente_registrado.nome == "Beatriz"
    assert cliente_registrado.tipo == "padrao"
    assert cliente_registrado.pontos == 50

def test_aplicar_bonus_promocional_em_compra():
    cliente = Cliente(nome="Diego", tipo="premium", pontos=0)
    sistema = SistemaPontuacao()

    valor_compra = 200.00
    bonus_percentual = 0.20
    pontos_esperados = 200 * 1.5 + (200 * 1.5 * bonus_percentual)

    pontos_calculados = sistema.calcular_pontos_com_bonus(cliente, valor_compra, bonus_percentual)

    assert pontos_esperados == pontos_calculados

def test_expirar_pontos_antigos_apos_periofodo():
    cliente = Cliente(nome="Elena", tipo="vip", pontos=3000)
    sistema = SistemaPontuacao()

    meses_passados = 12

    sistema.test_expirar_pontos(cliente, meses_passados)

    assert cliente.pontos == 0

def test_registrar_varios_clientes_em_lista():
    gerenciador = GerenciadorCliente()
    cliente1 = Cliente(nome="Fabio", tipo="padrao", pontos=100)
    cliente2 = Cliente(nome="Gabriela", tipo="premium", pontos=200)

    gerenciador.adicionar_cliente(cliente1)
    gerenciador.adicionar_cliente(cliente2)

    cliente_registrado1 = gerenciador.buscar_cliente_por_nome("Fabio")
    cliente_registrado2 = gerenciador.buscar_cliente_por_nome("Gabriela")

    assert cliente_registrado1.nome == "Fabio"
    assert cliente_registrado2.nome == "Gabriela"




