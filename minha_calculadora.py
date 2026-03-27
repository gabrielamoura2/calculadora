def soma (a,b):
    return a + b

def sub (a,b):
    return a - b

def mult (a,b):
    return a * b


def main ():  # MAIN é a porta de entrada de um programa
    x = int (input ("x: "))
    y = int (input ("y: "))
    s = soma (x,y)
    subt = sub (x,y)
    multip = mult (x,y)
    print (f"Soma da alegria = {s}")
    print (f"Subtração da alegria= {subt}")
    print (f"Multiplicação = {multip}")


main ()