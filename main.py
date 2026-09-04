def somar(valor_principal, acrescimo):
    '''
        Adiciona o acréscimo ao valor principal

        Args:
            valor_principal (float): valor inicial da soma
            acrescimo (float): valor a ser adicionado ao valor inicial
        
        Returns:
            float: soma do valor principal e acréscimo
    '''
    return valor_principal + acrescimo

def subtrair(valor_principal, decrescimo):
    '''
        Realliza o decréscimo do valor principal

        Args:
            valor_principal (float): valor inicial da subtração
            decrescimo (float): valor a ser decrescido do valor inicial
        
        Returns:
            float: diferenã do valor principal e acréscimo
    '''
    return valor_principal - decrescimo

def testar_operacao_soma():
    # Arrange
    valor1 = 100.0
    valor2 = 50.0
    # Act
    resultado = somar(valor1, valor2)
    # Assert
    assert resultado == 150.0, "A soma falhou!"
    print("Teste de Soma: PASSOU!")

def testar_operacao_subtrair():
    # Arrange
    valor1 = 100.0
    valor2 = 50.0
    # Act
    resultado = subtrair(valor1, valor2)
    # Assert
    assert resultado == 50.0, "A subtração falhou!"
    print("Teste de Subtração: PASSOU!")

testar_operacao_soma()
testar_operacao_subtrair()