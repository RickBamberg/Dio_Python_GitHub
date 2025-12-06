"""
Verificando Palíndromos 🔄
Descrição: Verifica se uma palavra é um palíndromo (lê-se igual de trás para frente).
"""

def verificar_palindromo():
    print("=== Verificando Palíndromos ===")
    print("Digite uma palavra para verificar se é um palíndromo.\n")
    
    # Recebendo a palavra
    palavra = input("Digite uma palavra: ").strip()
    
    if not palavra:
        print("Erro: Por favor, digite uma palavra válida.")
        return None
    
    # Processando a palavra (removendo espaços e convertendo para minúsculas)
    palavra_processada = palavra.replace(" ", "").lower()
    
    # Invertendo a palavra
    palavra_invertida = palavra_processada[::-1]
    
    # Verificando se é palíndromo
    if palavra_processada == palavra_invertida:
        resultado = "É UM PALÍNDROMO"
    else:
        resultado = "NÃO É UM PALÍNDROMO"
    
    # Exibindo o resultado
    print(f"\n=== Análise ===")
    print(f"Palavra original: '{palavra}'")
    print(f"Palavra processada: '{palavra_processada}'")
    print(f"Palavra invertida: '{palavra_invertida}'")
    print(f"\nResultado: {palavra} {resultado}")
    
    # Exemplos de palíndromos
    exemplos = ["ovo", "arara", "radar", "ana", "reviver"]
    if palavra_processada in exemplos:
        print(f"Curiosidade: '{palavra}' é um exemplo clássico de palíndromo!")
    
    return {
        'palavra_original': palavra,
        'palavra_processada': palavra_processada,
        'palavra_invertida': palavra_invertida,
        'e_palindromo': palavra_processada == palavra_invertida
    }

# Executando a função
if __name__ == "__main__":
    verificar_palindromo()