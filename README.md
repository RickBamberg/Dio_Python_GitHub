# 📚 Teste Final - Curso Básico de Python

Este repositório contém 6 scripts Python desenvolvidos como teste final de Python utilizando o GitHub. Cada script demonstra conceitos fundamentais da linguagem Python como manipulação de strings, operações matemáticas, validação de entrada e lógica condicional.

---

## 📋 Scripts

### 1️⃣ **01_concatenando_dados.py** 🐾

**Descrição:** Recebe dois dados diferentes do usuário e os concatena em uma única string.

**Conceitos Abordados:**
- Entrada de dados com `input()`
- Operador de concatenação `+`
- Função `type()` para verificar tipo de dados
- F-strings para formatação

**Como Usar:**
```bash
python 01_concatenando_dados.py
```

**Exemplo de Execução:**
```
=== Concatenando Dados ===
Digite o primeiro dado: Olá
Digite o segundo dado: Mundo

Resultado da concatenação: OláMundo
Tipo do resultado: <class 'str'>
```

---

### 2️⃣ **02_repetindo_textos.py** ✏️

**Descrição:** Recebe uma string e um número inteiro, retorna a string repetida o número de vezes informado.

**Conceitos Abordados:**
- Entrada validada com `try/except`
- Operador de repetição `*`
- Estrutura `while` para validação
- Validação de entrada do usuário

**Como Usar:**
```bash
python 02_repetindo_textos.py
```

**Exemplo de Execução:**
```
=== Repetindo Textos ===
Digite um texto: Python
Digite quantas vezes repetir: 3

Texto repetido 3 vezes: PythonPythonPython
```

---

### 3️⃣ **03_operacoes_matematicas.py** 📐

**Descrição:** Recebe dois números e realiza operações matemáticas básicas entre eles (soma, subtração, multiplicação e divisão).

**Conceitos Abordados:**
- Conversão de tipo com `float()`
- Operadores aritméticos: `+`, `-`, `*`, `/`
- Tratamento de divisão por zero
- Estrutura condicional `if/else`
- Retorno de múltiplos valores em dicionário

**Como Usar:**
```bash
python 03_operacoes_matematicas.py
```

**Exemplo de Execução:**
```
=== Operações Matemáticas ===
Digite o primeiro número: 10
Digite o segundo número: 3

=== Resultados ===
Números: 10.0 e 3.0
Soma: 10.0 + 3.0 = 13.0
Subtração: 10.0 - 3.0 = 7.0
Multiplicação: 10.0 × 3.0 = 30.0
Divisão: 10.0 ÷ 3.0 = 3.333...
```

---

### 4️⃣ **04_verificando_pares_impares.py** 🧮

**Descrição:** Recebe um número inteiro e verifica se é par ou ímpar utilizando o operador módulo.

**Conceitos Abordados:**
- Conversão com `int()`
- Operador módulo `%`
- Estrutura condicional `if/else`
- Tratamento de exceções `ValueError`
- Explicação da lógica matemática

**Como Usar:**
```bash
python 04_verificando_pares_impares.py
```

**Exemplo de Execução:**
```
=== Verificando Números Pares e Ímpares ===
Digite um número inteiro: 7

O número 7 é ÍMPAR.

Explicação:
Um número é par quando o resto da divisão por 2 é igual a 0.
7 % 2 = 1
```

---

### 5️⃣ **05_calculando_media_notas.py** 📚

**Descrição:** Calcula a média de três notas fornecidas pelo usuário e determina a situação acadêmica (aprovado, recuperação ou reprovado).

**Conceitos Abordados:**
- Estrutura `for` com `range()`
- Listas e operação `append()`
- Função `sum()` para somar elementos
- Validação com intervalos (`0 <= nota <= 10`)
- Múltiplas condições `if/elif/else`
- Formatação de números com `.2f`

**Critérios de Situação:**
- Média ≥ 7: **APROVADO** ✅
- Média 5 a 6,9: **RECUPERAÇÃO** ⚠️
- Média < 5: **REPROVADO** ❌

**Como Usar:**
```bash
python 05_calculando_media_notas.py
```

**Exemplo de Execução:**
```
=== Calculando Média de Notas ===
Digite a 1ª nota (0-10): 8.5
Digite a 2ª nota (0-10): 9.0
Digite a 3ª nota (0-10): 7.5

=== Resultado ===
Notas informadas: 8.5, 9.0, 7.5
Soma das notas: 25.0
Média: 25.0 ÷ 3 = 8.33
Situação: APROVADO
```

---

### 6️⃣ **06_verificando_palindromos.py** 🔄

**Descrição:** Verifica se uma palavra é um palíndromo (uma palavra que se lê igual de trás para frente).

**Conceitos Abordados:**
- Método `strip()` para remover espaços
- Método `lower()` para converter em minúsculas
- Método `replace()` para remover caracteres
- Slicing com `[::-1]` para inverter strings
- Operador de comparação `==`
- Listas e verificação com `in`

**Exemplos de Palíndromos:**
- ovo
- arara
- radar
- ana
- reviver

**Como Usar:**
```bash
python 06_verificando_palindromos.py
```

**Exemplo de Execução:**
```
=== Verificando Palíndromos ===
Digite uma palavra: Radar

=== Análise ===
Palavra original: 'Radar'
Palavra processada: 'radar'
Palavra invertida: 'radar'

Resultado: Radar É UM PALÍNDROMO
Curiosidade: 'radar' é um exemplo clássico de palíndromo!
```

---

### 🚀 **executar_todos.py**

**Descrição:** Script que executa todos os 6 programas em sequência, permitindo testar toda a bateria de exercícios de uma vez.

**Conceitos Abordados:**
- Módulo `subprocess` para executar scripts externos
- Módulo `sys` para acessar o Python atual
- Módulo `os` para verificar existência de arquivos
- Estrutura `for` para iteração
- Tratamento de exceções `CalledProcessError` e `KeyboardInterrupt`

**Como Usar:**
```bash
python executar_todos.py
```

---

## 🛠️ Requisitos

- Python 3.6 ou superior

## 📦 Como Executar

### Executar um script individual:
```bash
python 01_concatenando_dados.py
```

### Executar todos os scripts:
```bash
python executar_todos.py
```

---

## 📚 Conceitos Python Cobertos

| Conceito | Scripts |
|----------|---------|
| Entrada de dados | Todos |
| Strings e concatenação | 01, 06 |
| Operadores aritméticos | 03 |
| Operador módulo (%) | 04 |
| Estruturas condicionais (if/elif/else) | 03, 04, 05, 06 |
| Loops (for, while) | 02, 05 |
| Listas | 05, 06 |
| Validação de entrada | 02, 03, 04, 05 |
| Tratamento de exceções | 02, 03, 04 |
| Funções e retorno de valores | Todos |
| Formatação de strings | Todos |
| Slicing | 06 |
| Métodos de string | 06 |

---

## 🎓 Conclusão

Estes scripts representam uma progressão de conceitos fundamentais de Python, começando com operações simples de strings e chegando a lógica mais complexa com validações e manipulação de dados. São excelentes para consolidar os conhecimentos básicos da linguagem.

---

**Desenvolvido como teste final de Python utilizando o GitHub** 🐍✨
