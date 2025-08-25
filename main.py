def encontrar_maior_numero(lista_de_numeros):
    """
    Esta função recebe uma lista de números e retorna o maior número.
    Se a lista estiver vazia, retorna None.
    """
    # Verifica se a lista não está vazia para evitar erros
    if not lista_de_numeros:
        return None

    # Assume que o primeiro elemento é o maior
    maior_numero = lista_de_numeros[0]

    # Itera sobre o restante dos elementos da lista
    # Começamos do segundo elemento (índice 1)
    for numero in lista_de_numeros[1:]:
        # Compara o número atual com o maior número encontrado até agora
        if numero > maior_numero:
            # Se o número atual for maior, ele se torna o novo maior
            maior_numero = numero

    return maior_numero

# --- Exemplos de uso ---

# Exemplo 1: Lista com números positivos
numeros_1 = [5, 12, 9, 3, 25, 8]
maior_1 = encontrar_maior_numero(numeros_1)
print(f"O maior número na lista {numeros_1} é: {maior_1}")

# Exemplo 2: Lista com números negativos e positivos
numeros_2 = [-10, -5, -2, -15, 0]
maior_2 = encontrar_maior_numero(numeros_2)
print(f"O maior número na lista {numeros_2} é: {maior_2}")

# Exemplo 3: Lista com um único elemento
numeros_3 = [42]
maior_3 = encontrar_maior_numero(numeros_3)
print(f"O maior número na lista {numeros_3} é: {maior_3}")

# Exemplo 4: Lista vazia
numeros_4 = []
maior_4 = encontrar_maior_numero(numeros_4)
print(f"O maior número na lista {numeros_4} é: {maior_4}")