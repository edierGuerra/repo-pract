print("Calculadora")

#solicitar numeros
def solicitar_numeros():
    print("Ingresa los dos digitos \n")
    numeros=[]
    for i in range(2):
        numero = int(input(f"Ingresa el numero {i+1}: "))
        numeros.append(numero)
    return numeros
        
    
    
#almacenando numeros


#menu

def menu():
    listaNumeros = solicitar_numeros()
    n1 = listaNumeros[0]
    n2 = listaNumeros[1]
    o= input("""Que deseas hacer
        1. sumar
        2. multiplicar
        3. Restar
        4. Dividir\n""")
    if o =="3":
        print(restar(n1,n2))
    elif o == "2":
        print(multiplicar(n1,n2))
        
    


#funcion restar
def multiplicar(n1,n2):
    return n1 * n2

# funcion restar
def restar(n1,n2):
    return n1-n2


menu()
