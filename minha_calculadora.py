def soma (a,b):
    return a + b

def main ():  # MAIN é a porta de entrada de um programa
    x = int (input ("x: "))
    y = int (input ("y: "))
    s = soma (x,y)
    print (f"Soma = {s}")

main ()