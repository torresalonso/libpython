#coding: utf8
#Programa que implementa operaciones elementales sobre una matriz para convertirla en triangular superior
import os
import time

def imprimir_matriz(matriz):
    i=0
    while i<len(matriz):
        print (matriz[i])
        i+=1


#Definición de la función multiplo_escalar.
def multiplo_escalar(matriz_aux, renglon, escalar):
    j=0
    i=0

	#ciclo para multiplicar el renglón seleccionado por ESCALAR:
    for j in range(len(matriz_aux[0])):
        matriz_aux[renglon][j]*=escalar
	#una vez finalizado el ciclo, la matriz está lista y se devuelve;
    return matriz_aux

#Definición de la función sumar_multiplo_renglon.
def sumar_multiplo_renglon(matriz_aux,renglon_multiplo, renglon_modificar, escalar):
    j=0
    #declara un vector auxiliar donde guardaremos el renglón del cual queremos obtener un múltiplo (indicado con "renglon_multiplo).
    renglon_aux=[]
    for j in range(len(matriz_aux[0])):
        renglon_aux.append(matriz_aux[renglon_multiplo][j]*escalar)

    #Luego, éste lo sumaremos con el renglón indicado por renglon_modificar
    for j in range(len(matriz_aux[0])):
        matriz_aux[renglon_modificar][j]+=renglon_aux[j]

	#una vez finalizado el ciclo anterior, se devuelve la matriz con el renglón modificado
    return matriz_aux

#Definición de la función intercambiar renglones.
def intercambiar_rengones(matriz_aux,reng_pivote,col_pivote):
    i=0
    j=0
    #escanear los renglones bajo el pivote hasta hallar el primero con un elemento diferente de 0
    renglon_a_intercambiar=0
    for i in range(reng_pivote+1,len(matriz_aux)):
        if matriz_aux[i][reng_pivote]!=0:
            renglon_a_intercambiar = i
            break
    #intercambiar el renglón
    renglon_aux=[]
    for j in range(len(matriz_aux[0])):
        renglon_aux.append(matriz[renglon_a_intercambiar][j])

    for j in range(len(matriz_aux[0])):
        matriz_aux[renglon_a_intercambiar][j] = matriz_aux[reng_pivote][j]
        matriz_aux[reng_pivote][j] = renglon_aux[j]

    return matriz_aux

#Definición de la función convertir_triangular.
def convertir_triangular(matriz_aux):
    i=0
    j=0

    reng_pivote = 0
    col_pivote = 0
    while reng_pivote < filas:
        #el pivote es el primer elemento sobre la diagonal
        pivote = matriz_aux[reng_pivote][col_pivote]

        #si el pivote es 0, intercambiar renglones
        if(pivote == 0):
            intercambiar_rengones(matriz_aux, reng_pivote,col_pivote)
            pivote = matriz_aux[reng_pivote][col_pivote]

        #convertir los elementos bajo el pivote en 0
        for i in range(reng_pivote+1,filas):
            if(matriz_aux[i][col_pivote]!=0):
                sumar_multiplo_renglon(matriz_aux,reng_pivote,i,-(matriz_aux[i][col_pivote]/pivote))

        #pasar al siguiente pivote y repetir
        reng_pivote += 1
        col_pivote += 1

    return matriz_aux


#################################### Bloque de código que se ejecuta
i=0
j=0

filas = int(input("filas:"))
columnas = int(input("columnas:"))

matriz = [None] * filas
for i in range(filas):
    matriz[i] = [None] * columnas
os.system("clear")

#lectura de la matriz
for i in range(filas):
    for j in range(columnas):
        print "elemento M_",i,j
        matriz[i][j] = float(input())
        os.system("clear")

#se crea una matriz auxiliar para conservar la original.
matriz_aux = [None] * filas
for i in range(filas):
    matriz_aux[i] = [None] * columnas

#copiar la matriz en la auxiliar
for i in range(filas):
    for j in range (columnas):
        matriz_aux[i][j] = matriz[i][j]

print "matriz Original:"
imprimir_matriz(matriz_aux)
time.sleep(5)

print "\nMatriz reducida a triangular"
imprimir_matriz(convertir_triangular(matriz_aux))
