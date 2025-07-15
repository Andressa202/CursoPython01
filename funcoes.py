# Entendendo Funções em Python

def minhaFuncao() :
    print("Olá Mundo")

minhaFuncao()
minhaFuncao()
minhaFuncao()
minhaFuncao()

alunos = ['Jesreel', 'Eloara', 'Emily', 'Alice', 'Andressa','Davi']
cursos = ['Python', 'PHP', 'SQL']

# Trabalhando com variaveis de função
def minhaFuncaoMelhorada(animal, primaveras) :
    print("Você gosta de: ", animal, "e ele tem", str(primaveras) , "anos")
    # print("Você gosta de: " +  str(animal))

petCliente = input("Qual seu animal preferido? ")
idadePet = (input("Qual a idade do seu " + petCliente))
minhaFuncaoMelhorada (petCliente, idadePet)
minhaFuncaoMelhorada ("iguana", "4")
