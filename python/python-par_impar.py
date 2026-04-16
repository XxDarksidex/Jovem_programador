def parimpar(numero):
    if numero%2 == 0:
        return "par"
    else:
        return "impar"
        
while True:
    n1 = float(input("digite um numero(digite 0 para parar):"))
    if n1==0:
        break
        
    resultado = parimpar(n1)
    print(resultado)