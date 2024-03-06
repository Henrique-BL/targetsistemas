#Questão 5 - Resposta:
def inverter_string(s):
    # Inicializamos uma string vazia para armazenar o resultado
    resultado = ""
    
    # Percorremos a string da direita para a esquerda
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]  # Adicionamos o caractere atual ao resultado
    
    return resultado

# Exemplo de uso:
s_original = "Olá, Target Sistemas!"
s_invertida = inverter_string(s_original)
print(f"String original: {s_original}")
print(f"String invertida: {s_invertida}")
