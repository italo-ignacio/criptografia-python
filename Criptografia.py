import os
import time

tic = 1
a =1
veri=1

while True:
    if tic ==1:
        os.system('cls' if os.name == 'nt' else 'clear')
        if a == 1:
            co = input("Digite um numero inteiro para a base da cifra (1 a 5000)\nDigite> ")
            try:
                if int(co) > 5000 or int(co) <= 0:
                    veri = 2
                else:
                    veri = 1
            except:
                veri = 2
        if veri == 1:
            try:
                cod = int(co) *222
                os.system('cls' if os.name == 'nt' else 'clear')
                op = input('Digite 1 para criptogafar sua mensagem\nDigite 2 para descriptogafar sua mensagem\nDigite 3 para voltar\nDigite> ')
                if op =="1":
                    tic =5
                    a=1
                elif op=="2":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    tic =3
                    a=1
                elif op =="3":
                    a=1
                    tic=1
                else:
                    a=2
                    tic =1
            except:
                tic=1
        else:
            tic=1

    if tic == 2:
        print("\n")
        rep = input('Desaja retornar? (S/N)>') 
        if rep.upper() == ('N'):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("-------------------------------------------------------")
            print("               Foi bom enquanto durou\n")
            time.sleep(1)
            print("\n")
            print("                        3\n")
            time.sleep(1/2)
            print("\n")
            print("                        2\n")
            time.sleep(1/2)
            print("\n")
            print("                        1\n")
            time.sleep(1/2)
            print("\n")
            print("                       ADEUS!!!\n")
            time.sleep(1.5)
            break
        elif rep.upper() == ('S'):
            tic = 1
        else:
            tic = 2   

    if tic ==3:
        print("---------------  Descriptografar a Mensagem  ----------------\n") 
        menssagem = input('Mensagem a ser Descriptografada > ')
        try:
            if menssagem == "":
                print("\n\n")
                tic = 3
            else:
                print("\n")
                for i in range(len(menssagem)):
                    print(chr(ord(menssagem[i]) - cod),end='')
                tic = 2
        except:
            tic=4

    if tic == 4:
        print("\n")
        print("Não foi possivel descriptografar a mensagem\n")
        res = input('Deseja tentar novamente? (S/N)> ')
        print("\n")
        if res.upper() == "S":
            tic=3
        elif res.upper()=="N":
            tic=2
        else:
            tic=4

    if tic ==5:    
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-----------------  Criptografar a Mensagem  -----------------\n") 
        mensagem = input('Mensagem a ser Criptografada > ')
        print("\n")
        try:
            if mensagem=="":
                tic = 5
            else:
                for i in range(len(mensagem)):
                    print(chr(ord(mensagem[i]) + cod), end='')

                tic =3
                print("\n")
        except:
            tic = 6

    if tic == 6:
        print("Não foi possivel criptografar a mensagem\n")
        res = input('precione ENTER para tentar novamente')
        tic=5
