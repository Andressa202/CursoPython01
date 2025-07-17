# Importar o modulo unittest que nos permite escrever teste automatizados
import unittest 

#importar as funções teste
from teste_unitario import somar, subtrair,multiplicar,dividir

# criar a classe que contem os teste unitarios para as funções de operação 
class TesteOperacoes(unittest.TestCase):
    # testar a função de soma
    def testar_soma(self):
        #verificar se a soma de 2 e 3 é igual a 5 
        self.assertEqual(somar(2,3),5)

        #verificar se a soma de -1 e 1 é igual a 0
        self.assertEqual(somar(-1,1),0)

        #verificar se a soma de -2 e -3 é igual a -5
        self.assertEqual(somar(-2,-3),5)
    
    def testar_divisao(self):
        self.assertEqual(dividir(6,2),3)
        self.assertEqual(dividir(-6,3),-2)
        self.assertEqual(dividir(-6,-2),-3)
        with self.assertRaises(ValueError):
            dividir(1,0 ) # vai dar erro quando realizar o teste, pois não é possiel dividir por 0 


    def testar_multiplicar(self):
        self.assertEqual(multiplicar(2,2),4)
        self.assertEqual(multiplicar(3,2),6)
        self.assertEqual(multiplicar(5,5),26)
        

    def testar_subtrair(self):
        self.assertEqual(subtrair(6,2),4)
        self.assertEqual(subtrair(8,5),3)
        self.assertEqual(subtrair(5,2),2)
    

#permite que os testes sejam executados quando damos o arquivo diretamente
if __name__ == "__main__":
    unittest.main() #executa todos os testes definidos na class
