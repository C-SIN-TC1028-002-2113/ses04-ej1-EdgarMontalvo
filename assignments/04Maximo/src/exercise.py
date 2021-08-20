def main():
    #escribe tu código abajo de esta línea
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    num3 = int(input("Ingresa el tercer número: "))

    if num1>num2 and num1>num3:
        print("El mayor numero es", num1)
    elif num2>num3 and num2>3:
        print("El mayor numero es", num2)
    else:
        print("El mayor es", num3)
    
if __name__=='__main__':

    main()
