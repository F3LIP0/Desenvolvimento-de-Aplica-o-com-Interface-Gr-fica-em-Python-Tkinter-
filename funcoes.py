# Funções de conversão de unidades

def comprimento(valor, unidade_origem, unidade_destino):
    """
    Converte valores de comprimento entre diferentes unidades.
    
    Args:
        valor (float): Valor a ser convertido
        unidade_origem (str): Unidade de origem
        unidade_destino (str): Unidade de destino
    
    Returns:
        float: Valor convertido
    """
    # Converter tudo para metros primeiro
    metros = 0
    
    if unidade_origem == "Metros":
        metros = valor
    elif unidade_origem == "Centímetros":
        metros = valor / 100
    elif unidade_origem == "Milímetros":
        metros = valor / 1000
    elif unidade_origem == "Quilômetros":
        metros = valor * 1000
    
    # Converter de metros para a unidade de destino
    if unidade_destino == "Metros":
        return metros
    elif unidade_destino == "Centímetros":
        return metros * 100
    elif unidade_destino == "Milímetros":
        return metros * 1000
    elif unidade_destino == "Quilômetros":
        return metros / 1000
    
    return valor  # Fallback


def peso(valor, unidade_origem, unidade_destino):
    """
    Converte valores de peso entre diferentes unidades.
    
    Args:
        valor (float): Valor a ser convertido
        unidade_origem (str): Unidade de origem
        unidade_destino (str): Unidade de destino
    
    Returns:
        float: Valor convertido
    """
    # Converter tudo para gramas primeiro
    gramas = 0
    
    if unidade_origem == "Gramas":
        gramas = valor
    elif unidade_origem == "Quilogramas":
        gramas = valor * 1000
    elif unidade_origem == "Miligramas":
        gramas = valor / 1000
    
    # Converter de gramas para a unidade de destino
    if unidade_destino == "Gramas":
        return gramas
    elif unidade_destino == "Quilogramas":
        return gramas / 1000
    elif unidade_destino == "Miligramas":
        return gramas * 1000
    
    return valor  # Fallback


def temperatura(valor, unidade_origem, unidade_destino):
    """
    Converte valores de temperatura entre diferentes unidades.
    
    Args:
        valor (float): Valor a ser convertido
        unidade_origem (str): Unidade de origem
        unidade_destino (str): Unidade de destino
    
    Returns:
        float: Valor convertido
    """
    # Converter tudo para Celsius primeiro
    celsius = 0
    
    if unidade_origem == "Celsius":
        celsius = valor
    elif unidade_origem == "Fahrenheit":
        celsius = (valor - 32) * 5/9
    elif unidade_origem == "Kelvin":
        celsius = valor - 273.15
    
    # Converter de Celsius para a unidade de destino
    if unidade_destino == "Celsius":
        return celsius
    elif unidade_destino == "Fahrenheit":
        return celsius * 9/5 + 32
    elif unidade_destino == "Kelvin":
        return celsius + 273.15
    
    return valor  # Fallback


def formatar_resultado(valor):
    """
    Formata o resultado da conversão para exibição.
    
    Args:
        valor (float): Valor a ser formatado
    
    Returns:
        str: Valor formatado
    """
    # Se o valor for um número inteiro, mostra sem casas decimais
    if valor == int(valor):
        return str(int(valor))
    # Caso contrário, mostra com até 4 casas decimais, removendo zeros desnecessários
    else:
        return f"{valor:.4f}".rstrip('0').rstrip('.')

