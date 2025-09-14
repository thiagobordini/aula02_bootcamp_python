# Exercícios - Strings (str)

# 1) Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
nome_usuario = input("Digite o seu nome: ")
print(nome_usuario.upper())

# 2) Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome_usuario = input("Digite o seu nome completo: ")
print(nome_usuario.lower())

# 3) Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Digite uma frase: ")
print(frase.strip())

# 4) Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data_nasc = input("Digite sua data de nascimento (dd/mm/yyyy): ")
print(
    f"""
Dia: {data_nasc.split('/')[0]}
Mês: {data_nasc.split('/')[1]}
Ano: {data_nasc.split('/')[2]}
      """
)

# 5) Escreva um programa que concatene duas strings fornecidas pelo usuário.
nome_usuario = input("Digite o seu primeiro nome: ")
sobrenome_usuario = input("Digite o seu sobrenome: ")
print(nome_usuario + " " + sobrenome_usuario)
