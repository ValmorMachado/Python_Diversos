# Programa para verificar a maior nota de um participante de um concurso usando listas.
# Desenvolvido por Gustavo Miranda e Valmor Machado. INFNET 2021.
# Máteria de Lógica de programação. Professor: Carlos Pivotto.
# Última alteração: 12/04/2021
    
# ---------------------------------------- INICIO ----------------------------------------

# Listas vazias de nomes e notas.
nomes = []
notas = []

# Faz uma repetição para coletar os dados dos 6 participantes.
for d in range(1, 6):
    print("")
    # Inclui o nome na lista nomes.
    nomes.append(input(f'Informe o nome do {d}º participante: '))
    
    # Recebe a nota e valida.
    try:
        nota = int(input(f"Informe a nota do {d}º participante (Entre 0 e 10): "))
    except ValueError:
        nota = 0
    while nota == 0:
        nota = int(input(f'Atenção, Digite uma nota válida para o {d}º participante (Entre 0 e 10): '))
    # Inclui o nota na lista notas.
    notas.append(nota)

# O vencedor é o maior número da lista notas pego na função max.
nota_vencedor = max(notas)
# Para pegar o nome buscamos na lista nome pelo indice da maior nota.
nome_vencedor = nomes[notas.index(max(notas))]
print("")
print(f'O(A) Vencedor(a) é: {nome_vencedor} com a nota {nota_vencedor}!')
# ------------------------------------------ FIM ------------------------------------------
