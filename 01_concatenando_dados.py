"""
Concatenando Dados 🐾
Descrição: Recebe dois dados diferentes do usuário e os concatena em uma única string.
"""

def concatenar_dados():
    print("=== Concatenando Dados ===")
    print("Digite dois dados para concatená-los em uma única string.\n")
    
    # Recebendo os dois dados do usuário
    dado1 = input("Digite o primeiro dado: ")
    dado2 = input("Digite o segundo dado: ")
    
    # Concatenando os dados
    resultado = dado1 + dado2
    
    # Exibindo o resultado
    print(f"\nResultado da concatenação: {resultado}")
    print(f"Tipo do resultado: {type(resultado)}")
    return resultado

# Executando a função
if __name__ == "__main__":
    concatenar_dados()
    