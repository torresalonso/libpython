#coding: utf8
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

#Función convertir_triangular. Reduce una matriz cuadrada a una forma triangular sin convertir pivotes a 1
def convertir_triangular(matriz_aux, sup=1):
    #Si la matriz NO es cuadrada, no se continúa.
    if len(matriz_aux) != len(matriz_aux[0]):
        return None
    else:
        reng_pivote = 0
        col_pivote = 0
        i=0
        j=0

        while reng_pivote < filas:
            pivote = matriz_aux[reng_pivote][col_pivote]

            #si el pivote es 0, intercambiar renglón
            if(pivote == 0):
                intercambiar_rengones(matriz_aux, reng_pivote,col_pivote)
                pivote = matriz_aux[reng_pivote][col_pivote]

            #Si se pide superior (sup=1) convertir los elementos bajo el pivote en 0
            if sup == 1:
                for i in range(reng_pivote+1,filas):
                    if(matriz_aux[i][col_pivote]!=0):
                        sumar_multiplo_renglon(matriz_aux,reng_pivote,i,-(matriz_aux[i][col_pivote]/pivote))
            #Si se pide superior (sup=1) convertir los elementos sobre el pivote en 0
            else:
                for i in range(reng_pivote - 1,-1,-1):
                    if(matriz_aux[i][col_pivote]!=0):
                        sumar_multiplo_renglon(matriz_aux,reng_pivote,i,-(matriz_aux[i][col_pivote]/pivote))
            reng_pivote += 1
            col_pivote += 1

        return matriz_aux

def determinante(matriz_aux):
    if(len(matriz_aux) != len(matriz_aux[0])):
        return None
    else:
        det=1
        i = 0
        matriz_aux = convertir_triangular(matriz_aux,1)
        for i in range(len(matriz_aux)):
            det*=matriz_aux[i][i]
        return det


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

print "matriz Original:"
imprimir_matriz(matriz)

if determinante(matriz) != None :
    print "El determinante es ",determinante(matriz)
else:
    print "La matriz no es cuadrada"
