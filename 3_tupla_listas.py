#TUPLAS
#guarda elementos
#INMUTABLE= no va cambiar

#RECORRER TUPLAS

tupla=(25,1.65,'Reyna')
print(tupla[2])

indice=0



#while
while indice<len(tupla):
    print(tupla[indice])
    indice=indice+1


#for

tupla=(15,52,96,74)

for numeros in tupla:
    print(numeros)

#Posiciones de las tuplas

tupla=(12,55,85,96,74,92)
tupla2=tupla[0:3]
print(tupla2)

tupla3=tupla[:5]
print(tupla3)
