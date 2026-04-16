atividades

1_ nome = "maria"
idade = 18
cidade = "fraiburgo"
 
print (f"olá,meu nome é {nome}, tenho {idade} anos e moro no {cidade}")

2_ while True:
    numero1 = float(input("digite o º1 numero:"))

    numero2 = float(input("digite o º2 numero:"))

    operacao = input("digite a operação:")
    if operacao == ("+"):
        print(numero1 + numero2)
    elif operacao == ("-"):
        print(numero1 - numero2)
    elif operacao == ("*"):
        print(numero1 * numero2)
    elif operacao == ("/"):
        print(numero1 / numero2)
    elif operacao == "":
        break

3_numero = int(input("digite um numero:"))
for i in range(numero,numero*11,numero):
    print(i)

4_while True:
    tela = int(input("digite um numero, se acertar ganha:"))
    
    numero = 7
    if tela > numero:
        print("o numero é menor")
    elif tela < numero:
        print("o numero e maior ")
    else:
        print("voce acertou!!")
        break

5_lista = []

for i in range(5):
    mercado = input("digite 5 items:")
    lista.append(mercado)
print (lista)    

7_while True:
    numero = float(input("digite um numero(digite '-1' para sair):"))
    if numero %2 == 0:
        print("par")
    elif numero == -1:
        break
    else:
        print("impar")