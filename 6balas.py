from time import sleep
from random import randint
while True:
    print ("="*30)
    print ('     BEM-VINDO AO 6 BALAS')
    print ("="*30)
    bala = randint (1, 6)
    tiro = 0
    pa = 3
    morte = 3
    ganhou = True
    pronto = input("Pronto para começar [Y/N]? ").upper()
    if pronto == "Y":
        print ("Ok, as regras são simples...")
        sleep(2)
        print ("Há 1 bala em um révolver com 6 espaços...")
        sleep(2)
        print ("Você tem que apertar o gatilho para si mesmo 3 vezes...")
        sleep(2)
        print ("A cada rodada o tambor roda uma vez...")
        sleep(2)
        print ("Se não disparar, você ganha!")
        sleep(2)
        print ("Mas se disparar...")
        sleep(2)
        print ("Aliás... se pular 3 vezes... morre!")
        sleep(2)
        if pa>0:
            while pa>0:
                a = input("Deseja apertar o gatilho [Y/N]: ").upper()
                if a == "Y":
                    tiro +=1
                    pa -=1
                    if tiro == bala:
                        print("Perdeu...")
                        ganhou = False
                        break
                    else:
                        if pa==0:
                            break
                        else:
                            if morte>0:  
                                print ("De novo campeão.")
                        sleep(2)
                else:
                    morte -=1
                    if morte>0:
                        if pa==0:
                            break
                        else:
                            print ("De novo campeão.")
                        tiro +=1
                        sleep(2)
                if morte == 0:
                    break
            if  morte == 0:
                ganhou = False
        if morte == 0:
            print ("Perdeu parceiro, eu disse para não pular...")
        else:
            print ("Parabéns, ganhaste!")
    j = input("Deseja jogar mais [Y/N]? ").upper()
    if j == "N":
        break