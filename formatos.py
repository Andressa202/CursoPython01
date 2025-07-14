# Detalhando Strings e usando formatos

nomeCompleto = "Andressa Cruz Miranda"
inicio = 0
fim = inicio + 9
#pega uma fração do texto nomeCompleto
print("---------------------")
print ("Meu nome é ",nomeCompleto[inicio:fim]) 

nome = input("Qual seu nome? ")
sobrenome = input("E qual seu sobrenome? ")
idade = input("E sua idade: ")
print("Seu nome é: ",nome +" " + sobrenome, "e você tem:" ,idade, ", Correto?" )

caixinha01 = int(input("Insira seu primeiro valor: "))
caixinha02 = int(input("Insira seu segundo valor: "))
print("A soma é igual a ", caixinha01 + caixinha02, 
      "\nA subtração é ", caixinha01 - caixinha02, 
      "\nA multiplicação é ", caixinha01 * caixinha02, 
      "\nE A divisão é ", round(caixinha01 / caixinha02, 2))

