"""
Repetindo Textos ✏️
Descrição: Recebe uma string e um número inteiro, retorna a string repetida o número de vezes informado.
"""

def repetir_texto():
    print("=== Repetindo Textos ===")
    print("Digite um texto e quantas vezes deseja repeti-lo.\n")
    
    # Recebendo a string e o número inteiro
    texto = input("Digite o texto: ")
    
    # Validando a entrada do número
    while True:
        try:
            numero = int(input("Digite quantas vezes repetir (número inteiro): "))
            if numero >= 0:
                break
            else:
                print("Por favor, digite um número não negativo.")
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
    
    # Repetindo o texto
    resultado = texto * numero
    
    # Exibindo o resultado
    print(f"\nTexto repetido {numero} vezes: {resultado}")
    return resultado

# Executando a função
if __name__ == "__main__":
    repetir_texto()