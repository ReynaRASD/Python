#ARCHIVOS

#LECTURA
#ESCRITURA
#ABRIR SIN BORRAR

def crearArchivo():
    archivo=open('datos.txt','w')
    archivo.close()

def escribirArchivo():
    archivo=open('datos.txt','a')
    archivo.write('Reyna RASD\n')
    archivo.write('5554926321')
    archivo.close

def leerArchivo():
    archivo=open('datos.txt', 'r')
    linea=archivo.readline()
    while linea!="":
        print (linea)
        linea=archivo.readline()
    archivo.close()

#crearArchivo()
#escribirArchivo()

leerArchivo()
