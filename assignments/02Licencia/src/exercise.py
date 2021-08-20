def main():
    #escribe tu código abajo de esta línea
    edad = int(input("Ingresa tu edad: "))
    ident= input("¿Tienes identificación oficial? (s/n): ")
   
    if edad > 18: 
        print("No cumples requisitos")
     
    elif ident == "n":
        print("No cumples requisitos")

    elif ident == "s" :
        print("Trámite de licencia concedido")
    
    else:
        resultado= "ERROR"
    



if __name__ == '__main__':
    main()
