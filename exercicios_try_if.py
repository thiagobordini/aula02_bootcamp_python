# Exercício 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve
# solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a
# entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou
# uma mensagem de erro se a entrada não for válida.

try:
    celsius = float(input("Digite a temperatura em celsius: "))
except ValueError as e:
    print("Deve-se digitar uma temperatura válida.")
except KeyboardInterrupt as e:
    print("\nSaindo do programa")
else:
    resultado = (celsius * 9 / 5) + 32
    print(f"Conversão para Fahrenheit: {resultado}")

# Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo
# (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações).
# Utilize try-except para garantir que a entrada seja uma string.
# Dica: Utilize a função isinstance() para verificar o tipo da entrada.

entrada = input("Digite uma palavra ou frase: ")
if isinstance(entrada, str):
    formatado = entrada.replace(" ", "").lower()
    if formatado == formatado[::-1]:
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")
else:
    print("Entrada inválida. Por favor, digite uma palavra ou frase.")

# Exercício 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um
# operador (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e
# entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no
# operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

try:
    num_1 = float(input("Digite o primeiro número: "))
    num_2 = float(input("Digite o segundo número: "))
    calculo = input("Digite o cálculo desejado (+, -, *, /): ").strip()

    if calculo == "+":
        print(f"A soma dos números digitados é {num_1 + num_2}")
    elif calculo == "-":
        print(f"A subtração dos números digitados é {num_1 - num_2}")
    elif calculo == "*":
        print(f"A multiplicação dos números digitados é {num_1 * num_2}")
    elif calculo == "/":
        print(f"A divisão dos números digitados é {num_1 / num_2}")
    else:
        print("Entrada inválida.")
except ValueError as e:
    print("Entrada de número inválida")
except ZeroDivisionError as e:
    print("Impossibilidade de divisão por zero")
except KeyboardInterrupt as e:
    print("\nSaindo do programa")


# Exercício 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número.
# Utilize try-except para assegurar que a entrada seja numérica e
# utilize if-elif-else para classificar o número como "positivo",
# "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".
try:
    num = float(input("Digite um número: "))

    if num < 0:
        if num % 2 == 0:
            print("O número é negativo e par")
        else:
            print("O número é negativo e ímpar")
    else:
        if num % 2 == 0:
            print("O número é ppsitivo e par")
        else:
            print("O número é ppsitivo e ímpar")
except ValueError as e:
    print("Entrada de número inválida")
except KeyboardInterrupt as e:
    print("\nSaindo do programa")

# Exercício 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula.
# O programa deve converter a string de entrada em uma lista de números inteiros.
# Utilize try-except para tratar a conversão de cada número e validar que cada elemento
# da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro,
# imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos,
# imprima a lista de inteiros.
entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")
