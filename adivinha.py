from random import randint
#  Jogo de adivinhação 

print("---------- Iniciando o Jogo de Adivinhação ---------")
aleatorio = randint(0, 100)
chute =  0 
chances = 10 
while chute != aleatorio : 
    chute = input("Chute um numero entre 1 á 100: ")
    if chute.isnumeric():
        chute = int(chute)
        chances = chances - 1 
        if chute == aleatorio:
            print("--------------------------")
            print("Parabéns, você venceu. O numero era: {} e voce ainda tinha {} chances".format(aleatorio, chances))
            print("--------------------------")
            break
        else :
            print("---------------------------")
            if chute > aleatorio:
                print("Você errou, Dica: é um numero menor")
            else:
                print("Você errou, Dica: é um numero maior")
            print("Você ainda tem {} chances".format(chances))
            print("---------------------------")
        if chances == 0 :
             print("---------------------------")
             print("######GAME OVER ######")
             print("Suas chances acabaram, você perdeu!")
             print("---------------------------")
             break
print("-----------Fim de jogo--------------")