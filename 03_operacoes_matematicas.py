"""
Operações Matemáticas Simples 📐
Descrição: Recebe dois números e realiza operações matemáticas básicas entre eles.
"""

def operacoes_matematicas():
    print("=== Operações Matemáticas ===")
    print("Digite dois números para realizar operações matemáticas básicas.\n")
    
    # Recebendo os dois números
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: Por favor, digite números válidos.")
        return None
    
    # Realizando as operações
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    
    # Tratando a divisão por zero
    if num2 != 0:
        divisao = num1 / num2
    else:
        divisao = "Indefinida (divisão por zero)"
    
    # Exibindo os resultados
    print(f"\n=== Resultados ===")
    print(f"Números: {num1} e {num2}")
    print(f"Soma: {num1} + {num2} = {soma}")
    print(f"Subtração: {num1} - {num2} = {subtracao}")
    print(f"Multiplicação: {num1} × {num2} = {multiplicacao}")
    print(f"Divisão: {num1} ÷ {num2} = {divisao}")
    
    return {
        'soma': soma,
        'subtracao': subtracao,
        'multiplicacao': multiplicacao,
        'divisao': divisao
    }

# Executando a função
if __name__ == "__main__":
    operacoes_matematicas()