# Desenvolvido por Valmor Machado. INFNET 2021
# Máteria de Lógica de programação. Professor: Carlos Pivotto.

#Desenvolva uma função que calcule a divisão de uma conta de consumo (conta de restaurante ou bar), em reais,
#considerando o número de pessoas que estavam consumindo e a taxa de serviço que será paga ao garçom.

#Ao usuário do programa serão solicitados o 'valor total do consumo', em reais, 'o número total de pessoas' e o
#'percentual do serviço prestado', entre 0 e 100.

#Fluxo de exceção: 

#O programa deve verificar se o número total de pessoas é maior do que zero.
#O programa deve verificar se o percentual do serviço está dentro do intervalo válido, de 0 a 100. 

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
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