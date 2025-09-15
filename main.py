# Aula 02 - Bootacamp Python (Jornada de Dados)

# Métodos em diferentes tipos de dados do Python

# str
nome = "Thiago"
nome_com_espaco = " Thiago "
email = "thiago@gmail.com"
print(f"Método 'upper()': {nome.upper()}")
print(f"Método 'lower()': {nome.lower()}")
print(f"Método '.strip()': {nome_com_espaco.strip()}")
print(f"Método '.split()': {email.split('@')}")

# int
num_1 = 5
num_2 = 5
print(f"Adição (+): {num_1 + num_2}")
print(f"Subtração (-): {num_1 - num_2}")
print(f"Multiplicação (*): {num_1 * num_2}")
print(f"Divisão (/): {num_1 / num_2}")
print(f"Resto da divisão (%): {num_1 % num_2}")

# float
num_3 = 5.5
num_4 = 5.5
print(f"Adição (+): {num_3 + num_4}")
print(f"Subtração (-): {num_3 - num_4}")
print(f"Multiplicação (*): {num_3 * num_4}")
print(f"Divisão (/): {num_3 / num_4}")
print(f"Potenciação (**): {num_3 ** num_4}")

# # bool
ativo = True
inativo = False
print(f"Método (and): {ativo and inativo}")
print(f"Método (or): {ativo or inativo}")
print(f"Método (not): {not ativo}")
print(f"Método (==): {ativo == inativo}")
print(f"Método (!=): {ativo != inativo}")

# Tratativas e Exceções - Type Error (Try/Except/Else/Finally)

# Divisão por zero
try:
    num_1 = 1
    num_2 = 0
    resultado = num_1 / num_2
except ZeroDivisionError as e:
    print(e)
# else:
#     # caso dê certo a tentativa
# finally:
#     # caso dê certo ou errado

# Tipo de dado
try:
    num_1 = 1
    print(len(num_1))
except TypeError as e:
    print(e)
# else:
#     # caso dê certo a tentativa
# finally:
#     # caso dê certo ou errado

# Avaliação de tipos de dados - Type Check (isistance())

num = "1"
if isinstance(num, int):
    print("A variável 'num' é um inteiro")
else:
    print("A variável 'num' não é um inteiro")

# Conversão de tipo de dado - Type Conversion (Casting)

num = "19"
print(type(num))
print(type(int(num)))
