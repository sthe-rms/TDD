from app.cliente import calcular_pontos_compra_cliente_padrao


def test_calcular_pontos_compra_cliente_padrao():
    valor_da_compra = 100
    pontos = calcular_pontos_compra_cliente_padrao(valor_da_compra)
    assert pontos == 100