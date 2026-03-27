def soma (a,b):
    return a + b

def sub (a,b):
    return a - b

def main ():  # MAIN é a porta de entrada de um programa
    x = int (input ("x: "))
    y = int (input ("y: "))
    s = soma (x,y)
    subt = sub (x,y)
    print (f"Soma = {s}")
    print (f"Subtração = {subt}")


main ()