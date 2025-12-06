"""
Script para executar todos os 6 programas em sequência.
"""

import subprocess
import sys
import os

def executar_todos():
    scripts = [
        "01_concatenando_dados.py",
        "02_repetindo_textos.py",
        "03_operacoes_matematicas.py",
        "04_verificando_pares_impares.py",
        "05_calculando_media_notas.py",
        "06_verificando_palindromos.py"
    ]
    
    print("=== EXECUTANDO TODOS OS SCRIPTS ===\n")
    
    for script in scripts:
        if os.path.exists(script):
            print(f"\n{'='*50}")
            print(f"Executando: {script}")
            print(f"{'='*50}")
            
            # Executa o script usando o Python
            try:
                subprocess.run([sys.executable, script], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Erro ao executar {script}: {e}")
            except KeyboardInterrupt:
                print(f"\nExecução de {script} interrompida pelo usuário.")
                continuar = input("Deseja continuar com os próximos scripts? (s/n): ")
                if continuar.lower() != 's':
                    break
        else:
            print(f"Arquivo não encontrado: {script}")
    
    print(f"\n{'='*50}")
    print("Todos os scripts foram executados!")
    print(f"{'='*50}")

if __name__ == "__main__":
    executar_todos()
    