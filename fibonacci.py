# Questão 1: Sequência de Fibonacci

def fibonacci(n):
    """Calcula o n-ésimo número da sequência de Fibonacci.

    Args:
        n: O índice do número a ser calculado.

    Returns:
        O n-ésimo número da sequência de Fibonacci.
    """

    if n <= 0:
        return "O índice deve ser um número inteiro positivo."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Exemplo de uso:
numero = int(input("Digite um número: "))
resultado = fibonacci(numero)
print(f"O {numero}º número da sequência de Fibonacci é: {resultado}")

# Verifica se o número pertence à sequência
if numero in [fibonacci(i) for i in range(1, numero+1)]:
    print("O número pertence à sequência de Fibonacci.")
else:
    print("O número não pertence à sequência de Fibonacci.")