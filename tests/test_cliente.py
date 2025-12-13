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
    cliente = Cliente(nome="Lucas", tipo="padrao", pontos=0)
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

def test_expirar_pontos_antigos_apos_periododo():
    cliente = Cliente(nome="Elena", tipo="vip", pontos=3000)
    sistema = SistemaPontuacao()

    meses_passados = 12

    sistema.expirar_pontos(cliente, meses_passados)

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

#calcular pontos para todos os cliente de uma lista

def test_calcular_pontos_lista_clientes():
    sistema = SistemaPontuacao()

    clientes = [
        Cliente( nome = "ana", tipo = "padrao", pontos = 0),
        Cliente( nome = "theo", tipo = "premium", pontos = 0),
        Cliente( nome = "lara", tipo = "vip", pontos = 0)
    ]

    valor_compra = 100.00

    sistema.calcular_pontos_lista_clientes(clientes, valor_compra)
    assert clientes[0].pontos ==100.00
    assert clientes[1].pontos == 150.00
    assert clientes[2].pontos == 200.00

#filtrar cliente comsaldo de pontos superior ao valor determinado
def test_filtrar_clientes_com_pontos_acima_de_limite():
    gerenciador = GerenciadorCliente()

    cliente1 = Cliente( nome = "ana", tipo = "padrao", pontos = 100)
    cliente2 = Cliente( nome = "theo", tipo = "premium", pontos = 500)
    cliente3 = Cliente( nome = "lara", tipo = "vip", pontos = 1000)

    gerenciador.adicionar_cliente(cliente1)
    gerenciador.adicionar_cliente(cliente2)
    gerenciador.adicionar_cliente(cliente3)

    limite = 400

    clientes_filtrados = gerenciador.filtrar_clientes_com_pontos_acima_de_limite(limite)

    assert len(clientes_filtrados) == 2
    assert cliente2 in clientes_filtrados
    assert cliente3 in clientes_filtrados

# ordenar clientes pelo total de pontos acumulados
def test_ordenar_clientes_por_pontos():
    gerenciador = GerenciadorCliente()

    cliente1 = Cliente( nome = "ana", tipo = "padrao", pontos = 300)
    cliente2 = Cliente( nome = "theo", tipo = "premium", pontos = 100)
    cliente3 = Cliente( nome = "lara", tipo = "vip", pontos = 500)

    gerenciador.adicionar_cliente(cliente1)
    gerenciador.adicionar_cliente(cliente2)
    gerenciador.adicionar_cliente(cliente3)

    clientes_ordenados = gerenciador.ordenar_clientes_por_pontos()

    assert clientes_ordenados[0].nome == "lara"
    assert clientes_ordenados[1].nome == "ana"
    assert clientes_ordenados[2].nome == "theo"


# remover cliente que tem saldo de pontos = 0
def test_remover_clientes_com_saldo_zero():
    gerenciador = GerenciadorCliente()

    cliente1 = Cliente( nome = "ana", tipo = "padrao", pontos =0)
    cliente2 = Cliente( nome = "theo", tipo = "premium", pontos = 100)
    cliente3 = Cliente( nome = "lara", tipo = "vip", pontos = 0)
    cliente4 = Cliente( nome = "lia", tipo = "padrao", pontos = 50)
    cliente5 = Cliente( nome = "ney", tipo = "premium", pontos = 0)
   

    gerenciador.adicionar_cliente(cliente1)
    gerenciador.adicionar_cliente(cliente2)
    gerenciador.adicionar_cliente(cliente3)
    gerenciador.adicionar_cliente(cliente4)
    gerenciador.adicionar_cliente(cliente5)
    

    gerenciador.remover_clientes_com_saldo_zero()

    clientes_restantes = gerenciador.clientes

    assert len(clientes_restantes) == 2
    assert cliente2 in clientes_restantes
    assert cliente4 in clientes_restantes
    assert cliente1 not in clientes_restantes
    assert cliente3 not in clientes_restantes
    assert cliente5 not in clientes_restantes

# persquisar clentes pelo nome
def teste_buscar_cliente_por_nome():

    gerenciador = GerenciadorCliente()

    cliente1 = Cliente( nome = "ana", tipo = "padrao", pontos = 300)
    cliente2 = Cliente( nome = "theo", tipo = "premium", pontos = 100)
    cliente3 = Cliente( nome = "lara", tipo = "vip", pontos = 500)

    gerenciador.adicionar_cliente(cliente1)
    gerenciador.adicionar_cliente(cliente2)
    gerenciador.adicionar_cliente(cliente3)

    cliente_encontrado = gerenciador.buscar_cliente_por_nome("theo")

    assert cliente_encontrado == cliente2
    assert cliente_encontrado.nome == "theo"
    assert cliente_encontrado.tipo == "premium"
    assert cliente_encontrado.pontos == 100

   
# calcular o total de pontos de todos da lista

def test_somar_total_pontos_lista():

    gerenciador = GerenciadorCliente()

    cliente1 = Cliente( nome = "ana", tipo = "padrao", pontos = 300)
    cliente2 = Cliente( nome = "theo", tipo = "premium", pontos = 100)
    cliente3 = Cliente( nome = "lara", tipo = "vip", pontos = 500)

    gerenciador.adicionar_cliente(cliente1)
    gerenciador.adicionar_cliente(cliente2)
    gerenciador.adicionar_cliente(cliente3)

    total_pontos = gerenciador.somar_total_pontos_lista()
    assert total_pontos == 300 + 100 + 500

#ranking dos cliente com pontuaçao decrescente

def test_ranking_clientes_por_pontos():

    gerenciador = GerenciadorCliente()

    cliente1 = Cliente( nome = "ana", tipo = "padrao", pontos =300)
    cliente2 = Cliente( nome = "theo", tipo = "premium", pontos = 100)
    cliente3 = Cliente( nome = "lara", tipo = "vip", pontos = 500)
    cliente4 = Cliente( nome = "lia", tipo = "padrao", pontos = 50)
    cliente5 = Cliente( nome = "ney", tipo = "premium", pontos = 1000)
 
    gerenciador.adicionar_cliente(cliente1)
    gerenciador.adicionar_cliente(cliente2)
    gerenciador.adicionar_cliente(cliente3)
    gerenciador.adicionar_cliente(cliente4)
    gerenciador.adicionar_cliente(cliente5)
    

    ranking = gerenciador.ranking_clientes_por_pontos()
 
    assert ranking[0].nome == "ney"
    assert ranking[1].nome == "lara"
    assert ranking[2].nome == "ana"
    assert ranking[3].nome == "theo"
    assert ranking[4].nome == "lia"

# pontos expiram 10% apos 1 mes
def test_expirar_pontos_apos_um_mes():
    sistema = SistemaPontuacao()
    cliente = Cliente(nome="ney", tipo="premium", pontos=1000)

    sistema.expirar_pontos(cliente, 1)

    pontos_esperados = 900

    assert cliente.pontos == pontos_esperados

# todos pontos expiram apos 2 mes
def test_expirar_todos_os_pontos_apos_dois_meses():
    sistema = SistemaPontuacao()
    cliente = Cliente(nome="ney", tipo="premium", pontos=1000)

    meses_passados = 2

    sistema.expirar_pontos(cliente, meses_passados)

    assert cliente.pontos == 0

    

