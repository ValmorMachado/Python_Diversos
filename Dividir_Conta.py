# QUESTÃO 1 TP3
#Desenvolva uma função que calcule a divisão de uma conta de consumo (conta de restaurante ou bar), em reais,
#considerando o número de pessoas que estavam consumindo e a taxa de serviço que será paga ao garçom.

#Ao usuário do programa serão solicitados o 'valor total do consumo', em reais, 'o número total de pessoas' e o
#'percentual do serviço prestado', entre 0 e 100.

#Fluxo de exceção: 

#O programa deve verificar se o número total de pessoas é maior do que zero.
#O programa deve verificar se o percentual do serviço está dentro do intervalo válido, de 0 a 100. 
#Caso valores inválidos sejam digitados, deve ser exibida a mensagem de erro “Valor inválido” e o programa deve ser interrompido.
# Dica: Em Python, o valor monetário calculado ao final pode ser informado, na função print(), usando vírgula como separador de
#casa decimal, em vez de pontos.

#Para isso, converta o valor final da conta em uma string, usando a função str() e, em seguida, substitua os pontos por vírgulas
#com replace('.',',').
#Exemplo:

#valor = 1.99 # Valor numérico 
#valor = str(valor) # Converte o valor para uma string
#valor.replace('.', ',') # Substitui pontos por vírgulas
#print(valor) # Imprimirá 1,99

#Exemplo de saída do programa:
#Informe o valor total do consumo: R$ 100.00
#Informe o total de pessoas: 2
#Informe o percentual do serviço, entre 0 e 100: 10
#O valor total da conta, com a taxa de serviço, será de R$ 110,00.
#Dividindo a conta por 2 pessoa(s), cada pessoa deverá pagar R$ 55,00.

#-------------------------------------------------------------------------
#------------------------------TP3 QUESTÃO 1------------------------------
#-------------------------------------------------------------------------

def Formatar_moeda(valor):
    a = '{:,.2f}'.format(float(valor))
    b = a.replace(',','v')
    c = b.replace('.',',')
    return c.replace('v','.')

def Calcular_divisao(consumo,q_pessoas,tx_servico):
    # Se for uma pessoa calcula apenas a taxa de serviço e soma com o consumo
    if q_pessoas == 1:
        print(f"(\nO valor da sua conta é R$ ",Formatar_moeda(consumo),".")
        print(f"(\nVocê informou que pagará",tx_servico,"% de gorjeta ao garçom.")
        print(f"(\nO valor da sua conta ficou R$ ",Formatar_moeda(consumo+(consumo*(tx_servico/100))))
    # Se for mais de uma pessoa
    else:
        print(f"\nA conta total foi de R$",Formatar_moeda(consumo),"e será dividido para",q_pessoas,"pessoas.")
        print(f"\nA taxa de serviço paga ao garçom será de",tx_servico,"%.")
        print(f"\nValor total da conta: R$",Formatar_moeda(consumo),". O valor total da taxa de serviço é de R$",Formatar_moeda(consumo*(tx_servico/100)),".\n O valor para cada pessoa será de R$",Formatar_moeda(((consumo/q_pessoas) + ((consumo*(tx_servico/100))/q_pessoas))),".")


print("----------------------------------------------------------------------------------------------------")
print("-------------------------------------- DIVIDINDO A CONTA -------------------------------------------")
print("----------------------------------------------------------------------------------------------------")

consumo = round(float(input(f"Gentileza, digite o valor da conta (exemplo: 850,12): ").replace(",",".")),2)

q_pessoas = int(input(f"Agora por favor, digite o número de pessoas em que será dividido a conta: "))

while q_pessoas < 0:
    q_pessoas = int(input(f"Número Inválido, por favor, digite o número de pessoas em que será dividido a conta novamente: "))

tx_servico = int(input("Para finalizar gentileza digitar o percentual desejado da taxa de serviço (de 0% a 100%): "))

while tx_servico < 0 or tx_servico > 100:
    tx_servico = input("Atenção, digite o percentual desejado da taxa de serviço entre 0% e 100%: ")

Calcular_divisao(consumo,q_pessoas,tx_servico)

print("----------------------------------------------------------------------------------------------------")
print("---------------------------------- OBRIGADO PELA PREFERÊNCIA ---------------------------------------")
print("----------------------------------------------------------------------------------------------------")