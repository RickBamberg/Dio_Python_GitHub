"""
Calculando Média de Notas 📚
Descrição: Calcula a média de três notas fornecidas pelo usuário.
"""

def calcular_media_notas():
    print("=== Calculando Média de Notas ===")
    print("Digite três notas para calcular a média.\n")
    
    notas = []
    
    # Recebendo as três notas
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Digite a {i}ª nota (0-10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Por favor, digite uma nota entre 0 e 10.")
            except ValueError:
                print("Por favor, digite um número válido.")
    
    # Calculando a média
    media = sum(notas) / len(notas)
    
    # Exibindo as notas e a média
    print(f"\n=== Resultado ===")
    print(f"Notas informadas: {notas[0]}, {notas[1]}, {notas[2]}")
    print(f"Soma das notas: {sum(notas)}")
    print(f"Média: {sum(notas)} ÷ {len(notas)} = {media:.2f}")
    
    # Verificando situação
    if media >= 7:
        situacao = "APROVADO"
    elif media >= 5:
        situacao = "RECUPERAÇÃO"
    else:
        situacao = "REPROVADO"
    
    print(f"Situação: {situacao}")
    
    return {
        'notas': notas,
        'media': media,
        'situacao': situacao
    }

# Executando a função
if __name__ == "__main__":
    calcular_media_notas()