Experimente agoraTente novamente mais tardeNão mostrar novamente
import random

print("*********************************")
print("Bem vindo ao jogo de adivinhação, melhor de três!")
print("*********************************")

#round: arredonda n°;  random: n° aleatório
#numero_secreto = round(random.random() * 100)

#var = n°aleatório.delimitado(começa,termina)
numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
#print(numero_secreto)

print("Qual nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Define o nível: "))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

#No for in range , declara-se a var rodada dentro do laço;
#Se faz necessário adicionar um +1 ao final do parâmetro p/ que vá até 3, caso contrário irá até 2;
# range(start, stop, [step])
for rodada in range(1, total_de_tentativas + 1):
    #P/ concatenar string chamando variável: utilizar {} vazio + .format(var1,var2,var3 etc)
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    chute_eh_maior = chute > numero_secreto
    chute_eh_menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    else:
        if(chute_eh_maior):
            print("Você errou! O seu chute foi maior do que o número secreto, tente um número menor!")
        elif(chute_eh_menor):
            print("Você errou! O seu chute foi menor do que o número secreto, tente um número maior!")

    rodada = rodada + 1

print("Fim do jogo! O número secreto era:",numero_secreto)

