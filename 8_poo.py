#POO=PROGRAMACION ORIENTADA A OBJETOS

#-CLASES
#-OBJETOS
#-PROPIEDADES
#-METODOS

#################################    CLASES

########  ATRIBUTOS


####    METODO


#las clases no se pueden quedar sin definir, o en todo caso ponerle pass para que no marque error

#clase
class Persona:
    #atributo
    nBrazo=0
    nPiernas=0
    cabello=True
    cCabello='Defecto'
    hambre=0

#Inicializador
    def __init__(self):
        self.nBrazos=2
        self.nPiernas=2
    
    #metodo
    def dormir():
        pass
    def comer(self):
        self.hambre=5

class Hombre(Persona):
    hombre='Defecto'
    sexo='M'
    def cambiarNombre(nombre):
        self.nombre=nombre

class Mujer(Persona):
    nombre='Defecto'
    sexo='F'

#Herencia
jose=Hombre()
jose.comer()
print(jose.hambre)


##################

class Rectangulo():
    altura=0
    base=0

    def calcularArea(self):
        return (self.altura*self.base)/2

    


