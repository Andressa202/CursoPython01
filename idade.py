# Exercício : idade 
# Perguntar anos de nasc e ano atual, retirnar idade e perguntar se deseja novo teste


executar = True
while executar : 
    anoNasc = int(input("Em que ano você nasceu? "))
    anoAtual = int(input("Em que ano estamos? "))
    idade = anoAtual - anoNasc
    print("Você tem: ", idade, "anos")
    pergunta = input("Deseja testar novamente? ")
    if pergunta == "não":
         executar = False


# Mesma coisa, porém mais bonitinho 
"""
executar = True
while executar : 
    anoNasc = int(input("Em que ano você nasceu? "))
    anoAtual = int(input("Em que ano estamos? "))
    idade = anoAtual - anoNasc
    print("Você tem: ", idade, "anos")
    pergunta = input("\n Deseja testar novamente? \n [1]SIM \n [2]NÃO \n")
    if pergunta == "2":
         executar = False
"""
print("----------- Segundo Exercicio Usando Funções-------------")

def calcular_idade() :
    anoNsc = int(input("Em que ano você nasceu? "))
    anoAtl = int(input("Em que ano estamos? "))
    idade = anoAtl - anoNsc
    print("Você tem " + str(idade) + "anos. ")

def perguntar_novamente():
    opcao = input("deseja testar novamente? sim ou Não: ")
    if opcao.lower() in ["Sim", "s"] : 
        iniciarprograma()
    else: 
        print("Encerrando programa! Até mais 😎")

def iniciarprograma():
    calcular_idade()
    perguntar_novamente()

# Chamada inicial
iniciarprograma()


     