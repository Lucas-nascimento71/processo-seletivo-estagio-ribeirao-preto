# Questão 2: Contagem de ocorrências da letra 'a'

def contar_as(texto):
    """Conta o número de ocorrências da letra 'a' (maiúscula ou minúscula) em uma string.

    Args:
        texto: A string a ser analisada.

    Returns:
        O número de ocorrências da letra 'a'.
    """

    return texto.lower().count('a')

# Exemplo de uso:
texto = input("Digite uma frase: ")
quantidade_as = contar_as(texto)
print(f"A letra 'a' aparece {quantidade_as} vezes no texto.")