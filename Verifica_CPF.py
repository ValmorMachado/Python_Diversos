# Desenvolvido por Valmor Machado. INFNET 2021
# Máteria de Lógica de programação. Professor: Carlos Pivotto.

# Programa para verificar um CPF

print("---------------------------------------------------------------------------------")
print("------------------------------ VERIFICADOR DE CPF -------------------------------")
print("---------------------------------------------------------------------------------")
print("")
# A pessoa digita o nome.
nome = input(f"Informe seu nome: ")

# Pede o valor do CPF e válida.
cpf = input(f"\nInforme seu CPF com 11 algarismos: ")

try:
    valor = int(cpf)
except ValueError:
    valor = 0
    
while len(cpf) < 11 or valor == 0:
    cpf = input(f"\nAtenção, Informe seu CPF com 11 algarismos: ")
    try:
        valor = int(cpf)
    except ValueError:
        valor = 0

# Separando os algarismos em uma lista.
digitos = list(cpf)

#Verificando o decimo digito do CPF

L = (10*int(digitos[0]) + 9*int(digitos[1]) + 8*int(digitos[2]) + 7*int(digitos[3]) + 6*int(digitos[4]) + 5*int(digitos[5]) + 4*int(digitos[6]) + 3*int(digitos[7]) + 2*int(digitos[8]))

# Pega o resto da divisão de L por 11
rL = (L%11)
# condição para achar o décimo digito do cpf
if rL == 0 or rL == 1:
    d10 = 0
else:
    d10 = int(11 - rL)

#Verificando o decimo primeiro digito do CPF

M = (10*int(digitos[1]) + 9*int(digitos[2]) + 8*int(digitos[3]) + 7*int(digitos[4]) + 6*int(digitos[5]) + 5*int(digitos[6]) + 4*int(digitos[7]) + 3*int(digitos[8]) + 2*int(digitos[9]))

# Pega o resto da divisão de M por 11
rM = (M%11)

# condição para achar o décimo primeiro digito do cpf
if rM == 0 or rM == 1:
    d11 = 0
else:
    d11 = int(11 - rM)

# Condição para saber se o cpf é verdadeiro
if d10 != int(digitos[9]) or d11 != int(digitos[10]):
    print("")
    print(f"\n{nome}, seu cpf é inválido!")
    print("")
else:
    print("")
    print(f"{nome}, seu cpf é válido!")
    print("")

print("---------------------------------------------------------------------------------")
print("---------------------------------- FIM ------------------------------------------")
print("---------------------------------------------------------------------------------")
# FIM DO PROGRAMA.
