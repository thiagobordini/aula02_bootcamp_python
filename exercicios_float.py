# Exercícios - Números de Ponto Flutuante (float)

# 1) Escreva um programa que receba dois números flutuantes e realize sua adição.
num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))
print(f"A soma dos valores digitados é {num_1 + num_2}\n")

# 2) Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))
print(f"A média dos valores digitados é {(num_1 + num_2) / 2}\n")

# 3) Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
num_1 = float(input("Digite o primeiro número (base): "))
num_2 = float(input("Digite o segundo número (expoente): "))
print(f"A potência da base digitada é {num_1 ** num_2}\n")

# 4) Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Digite a temperatura em celsius: "))
print(f"A conversão para Fahrenheit é {(celsius * 9/5) + 32}\n")


# 5) Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input("Digite o raio do círculo: "))
print(f"A área do circulo é {3.14 * (raio**2)}")
