
#Questão 2 - Resposta:
def fibonacci_sequence(n):
    # Inicializa os primeiros dois termos da sequência
    n1, n2 = 0, 1

    # Verifica se o número informado é igual a 0 ou 1
    if n in (n1, n2):
        return f"{n} pertence à sequência de Fibonacci."

    # Gera a sequência até encontrar um termo maior ou igual ao número informado
    while n2 < n:
        nth = n1 + n2
        n1, n2 = n2, nth

        # Se encontrarmos o número na sequência, retorna a mensagem
        if n2 == n:
            return f"{n} pertence à sequência de Fibonacci."

    # Se não encontrarmos o número, retorna outra mensagem
    return f"{n} não pertence à sequência de Fibonacci."

# Exemplo de uso
numero_informado = int(input("Informe um número: "))
print(fibonacci_sequence(numero_informado))
