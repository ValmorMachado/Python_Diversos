# Programa para verificar a maior nota de um participante de um concurso
# Usando listas
# Desenvolvido por Gustavo Miranda e Valmor Machado. INFNET 2021
# Máteria de Lógica de programação. Professor: Carlos Pivotto.
def tnota(nota):
    if nota < 0 or nota > 10:
        return False
    else:
        return True
nomes = []
notas = []

for d in range(1, 6):
    nomes.append(input(f'Informe o nome do {d}º participante: '))
    nota = int(input(f'Informe a nota do {d}º participante: '))
    
    while tnota(nota) != True:
        nota = int(input(f'Informe a nota do {d}º participante (Entre 0 e 10): '))
        
    notas.append(nota)
   
   
print(nomes)
print(notas)
nota_vencedor = max(notas)
nome_vencedor = nomes[notas.index(max(notas))]

print(f'O(A) Vencedor(a) é: {nome_vencedor} com a nota {nota_vencedor}!')