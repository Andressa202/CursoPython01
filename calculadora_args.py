# Calculadora com multiplos argumentos.

class calculadora:
    def somar(self, *args):
        return sum(args)
# Criar o objeto calculadora
calc = calculadora()

# passagem dos argumentos (Quantos desejar)

print(calc.somar(2,6) )# Retorna 8
print(calc.somar(1, 2, 3 ,4 , 5)) # Retorna 15