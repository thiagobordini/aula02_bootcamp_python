# Booleanos (bool)

# 1) Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
expressao_1 = input("Digite a primeira expressão booleana: ")
expressao_2 = input("Digite a segunda expressão booleana: ")
print(expressao_1 and expressao_2)


# 2) Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
expressao_1 = bool(input("Digite a primeira expressão booleana: "))
expressao_2 = bool(input("Digite a segunda expressão booleana: "))
print(expressao_1 or expressao_2)

# 3) Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
expressao = input("Digite a primeira expressão booleana: ")
print(not expressao)

# 4) Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
expressao_1 = input("Digite a primeira expressão booleana: ")
expressao_2 = input("Digite a segunda expressão booleana: ")
print(expressao_1 == expressao_2)

# 5) Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
num_1 = int(input("Digite o primeiro numero: "))
num_2 = int(input("Digite o segundo numero: "))
print(num_1 != num_2)
