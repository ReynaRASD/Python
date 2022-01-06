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

def sumar(numero1, numero2):
    resultado=numero1+numero2
    return resultado

valor=sumar(20, 20)
print(valor)

# valor por defecto, es colocar dentro del -def el numero2 igual a 0 u otro numero
# Si y solo si no recibe el valor ocupara ese valor.
# Se inicia de derecha a izquierda, orden de importancia.


