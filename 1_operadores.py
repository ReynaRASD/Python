print("codigo")
#Comentarios
#***************  Variables:
 #   -Enteros
  #  -Reales y/o flotantes
   # -Boolean
    #-Cadenas

edad=25
altura=1.65
nombre="Reyna"
sexofemenino=True

print("edad=", edad, "altura=", altura, "nombre=", nombre, "Femenino=", sexofemenino)

#Numero complejo
numeroc=7+8j
print(numeroc)

# -------------------Operadores matematicos
x=10
y=2

resultado=x+y
# signos: +, -, *, /, %, 
# La doble diagonal // redondea hacia abajo----> 5.9=5
# Signo de % es el residuo de una division

print(resultado)

# Para potencia

potencia=2**3

print (potencia)

#----------------Condicional
# identacion es el espacio dentro de una funcion o condicion, en Python es elemental usarlo, si se mueve cambia y esta mal

#   if(condicion)

pago=True

if edad>18:
    print('Si es mayor de edad')
    if edad!=18:
        print('Son diferentes')
    else:
        print('Son iguales')
    if pago==True:
        print('Eres mayor y pagaste')
    else:
        print('Eres mayor de edad y no pagaste')
else:
    print('No es mayor de edad')

#**************Condicionales anidadas=condicion dentro de otra
# == dos iguales es si son iguales



# -----------Operadores relacionales
#   > mayor
#    < menor
#    !=   son diferentes o contrario
#     ==    iguales


# -------------Operadores logicos
#   and (se cumplen una y otra, todas)     or (solo se cumple alguna)
#     not es la negacion, lo contrario de lo que pregunte

if edad>24 and edad<26:
    print('Tu edad es 25')
else:
    print('Tu edad no es 25')

if not edad>18:
    print('Si')
else:
    print('No')


# -------------------Sentencia WHILE

#while(Este lloviendo):
 #   usamos sombrilla

numero=1

while(numero<100):
    print('El valor de numero es:', numero)
    numero=numero+1
    #El while se utiliza siempre que sabemos que queremos, o lo que no queremos.





#Ejercicio

print('EJERCICIO')

entero1 = 11
entero2 = 2
num1 = 1.5
num2 = 5.0

suma = entero1 + entero2
multiplicacion = num1 * num2
division1 = entero1 / entero2;
division2 = entero1 % entero2;
division3 = num2 // entero2;

print(suma)
print(multiplicacion)
print(division1)
print(division2)
print(division3)



