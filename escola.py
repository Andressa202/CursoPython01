# Trabalhando com If , Else e  testes
tipoEscola = input("tipo do colégio: \n [1] - publico \n [2] - particular\n ")
freqAluno = int(input("Qual a frequência do aluno? "))
nomeAluno = input("Qual o nome do Aluno: ")
mediaEscola = float(input("Media de corte da Escola: "))
if tipoEscola == "2":
     print("------- Colégio Particular --------")

print("-----------------------------------")
if tipoEscola =="1":
     print("------ Escola publica ------ ")
p = float(input("Nota de Português: "))
m = float(input("Nota de matemática: "))
c = float(input("Nota de ciências: "))
media = (p + m + c)/3
print("------------------------------------")
print("essa foi a media do aluno",round(media,2),"e ele tem :", freqAluno,'%', "de presença","\nEntão ele esta:")
if tipoEscola == "2" and media >= mediaEscola and freqAluno>= 70:
     print("Aprovado")
else:
     print("Reprovado")
print("-----------------------------------")
if tipoEscola == "1" and  media >= mediaEscola and freqAluno >= 60: 
           print("Aprovado")
else:
     print("Reprovado")

