#PROGRAMA DE JOGO DE ALETORIADADEA
import random


pontuacao = random.randint(1, 100)
acerto=True
tentativas=0
while(acerto):
    print('=====================================')
    entrada=int(input("tente adivinha um numero de 1 a 100 :"))
    if pontuacao==entrada:
        acerto=False
    if entrada>pontuacao:
        print(' e menor cara !!' )
        tentativas +=1
    if entrada<pontuacao:
        print(' e maior cara !!' )
        tentativas +=1

print('voce acerto, e voce tentou {}'.format(tentativas))
print('=======================================')
