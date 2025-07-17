import numpy as np 

#Criar um array Numpy (vetor)
arr = np.array([1, 2, 3, 4, 5])
print("Array do Numpy")
print(arr)

# Operaçôes matematicas usando os arrays
print("\nArray multiplicar por 2")
print(arr * 2)

# Operações entre 2 arrays
arr2 = np.array([10, 20, 30, 40, 50])
print("\nArray 2 ")
print(arr2)
print("\nSoma entre arrays")
print(arr + arr2)

#Criar uma matriz (2d)
matriz = np.array([[1, 2, 3,],[4 ,5 ,6]])
print("\nMatrix 2x3")
print(matriz)

#Somar elementos da matriz 
print("\nSoma de todos os elementos da matriz")
print(np.sum(matriz))

#Media dos dados da matriz
print("\nMedia dos elementos da matriz")
print(np.mean(matriz))

#transposta da Matriz
print("\nMatriz transposta")
print(matriz.T)

#Gerar valores aleatorios 
print("\nNumeros aleatorios entre 0 e 1")
print(np.random.rand(3,3)) # gera uma matriz de 3x3 com valores aleatorios entre 0 e 1 


