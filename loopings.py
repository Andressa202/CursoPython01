# Trabalhando com Loopings

palavra = "garrafinha"
contador = 0
print("Palavra Escolhida: ", palavra)
for letra in palavra :
    print(contador,"-" ,letra)
    contador = contador + 1 
print("-----------------")
cidades = ["Salvador", "Lauro de Freitas", "Fortaleza", "São Paulo", "Londres", "Eastbourne", "Brighton"]
for cidade in cidades : 
    print(cidade)
print("----------------")
print(cidades[4])
print("------------ While -----------------")

botaoExecutar = True #valor boolean
contador = 0 
while botaoExecutar: 
    print(contador)
    contador = contador + 1 
    if contador >= 10 :
        botaoExecutar = False

print("---------------------------")

listaCompras = ["Tênis", "Calça Jeans", "Salto Alto", "Vestidos", "Camisetas", "Saias"]
contar =  1
for lista in listaCompras: 
    print('[' + str(contar) + ']' + lista)
    contar = contar + 1





        
