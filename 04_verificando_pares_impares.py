"""
Verificando Números Pares e Ímpares 🧮
Descrição: Recebe um número inteiro e verifica se é par ou ímpar.
"""

def verificar_par_impar():
    print("=== Verificando Números Pares e Ímpares ===")
    print("Digite um número inteiro para verificar se é par ou ímpar.\n")
    
    # Recebendo o número inteiro
    try:
        numero = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido.")
        return None
    
    # Verificando se é par ou ímpar
    if numero % 2 == 0:
        resultado = "PAR"
    else:
        resultado = "ÍMPAR"
    
    # Exibindo o resultado
    print(f"\nO número {numero} é {resultado}.")
    
    # Explicação adicional
    print(f"\nExplicação:")
    print(f"Um número é par quando o resto da divisão por 2 é igual a 0.")
    print(f"{numero} % 2 = {numero % 2}")
    
    return resultado

# Executando a função
if __name__ == "__main__":
    verificar_par_impar()