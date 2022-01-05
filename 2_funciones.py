print('FUNCIONES')

def saludo(nombre):
    print('Hola', nombre)
def comer():
    print('Comer')

saludo('Jose')
saludo('Reyna')

usuario='Chucho'
saludo(usuario)


#Ejercicio
print('Ejercicio, regreso de datos')

def sumar(numero1, numero2=0):
    resultado=numero1+numero2
    return resultado

valor=sumar(200)
print(valor)

# valor por defecto, es colocar dentro del -def el numero2 igual a 0
# Se inicia de derecha a izquierda, orden de importancia.


