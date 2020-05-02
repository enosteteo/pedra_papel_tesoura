import random

poderes = ["pedra", "papel", "tesoura"]
jogador_1_vitorias = 0
jogador_2_vitorias = 0
empates = 0
partida = 0
fim = False
while not fim:
    partida += 1
    jogador_2 = random.randint(0, (len(poderes) - 1))

    jogador_1 = input("Pedra Papel ou Tesoura?! ").lower()
    if jogador_1 not in poderes:
        fim = True
        break
    for i in range(len(poderes)):
        if jogador_1 == poderes[i]:
            jogador_1 = i
    if jogador_1 < jogador_2 and jogador_1 != 0:
        if jogador_1 != 0:
            jogador_2_vitorias += 1
            print("jog 2 %i " % jogador_2_vitorias)
        else:
            jogador_1_vitorias += 1
            print("jog 1 %i " % jogador_1_vitorias)
    elif jogador_2 < jogador_1 and jogador_2 != 0:
        if jogador_2 != 0:
            jogador_1_vitorias += 1
            print("jog 1 %i " % jogador_1_vitorias)
        else:
            jogador_2_vitorias += 1
            print("jog 2 %i " % jogador_2_vitorias)
    else:
        print(empates)
        empates += 1
        partida = 0
    if partida == 10:
        fim = True
if jogador_1_vitorias > jogador_2_vitorias:
    print("jogador 1 venceu!")
elif jogador_2_vitorias > jogador_1_vitorias:
    print("jogador 2 venceu!")
else:
    print("Foi muito desafiador! ainda assim você conseguiu o empate!")
print("Obrigado por ter jogado conosco!")
