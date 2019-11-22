#coding: utf8
import os
import time

def imprimir_matriz(matriz):
    i=0
    while i<len(matriz):
        print (matriz[i])
        i+=1

def prod_int(u,v):
    i = 0
    n = len(u)
    prod = 0
    while i < n:
        prod += u[i]*v[i]
        i+=1
    return prod

def prod_mat(matrizA,matrizB):
    i=0
    j=0
    k=0
    renglon_i=[]
    columna_j=[]

    #verifica que el producto pueda hacerse; en tal caso, se procede al producto
    if len(matrizA[0]) == len(matrizB):

        #Creación de la matriz resultante
        matrizAB = [None] * len(matrizA)
        for i in range(len(matrizA)):
            matrizAB[i] = [None] * len(matrizB[0])

        #vectores renglón i-ésimo de la matriz A y columna j-ésima de la matriz B
        for k in range(len(matrizA[0])):
            renglon_i.append(0)
        for k in range(len(matrizB)):
            columna_j.append(0)

        #recorrer la matriz resultante; en su elemento ij-ésimo se introducirá el producto <renglon_i,columna_j>
        for i in range (len(matrizAB)):
            for j in range (len(matrizAB[0])):
                #armar los vectores renglón y columna
                for k in range(len(matrizA[0])):
                    renglon_i[k] = matrizA[i][k]
                for k in range(len(matrizB)):
                    columna_j[k] = matrizB[k][j]
                #realizar el producto
                matrizAB[i][j] = prod_int(renglon_i,columna_j)
        imprimir_matriz(matrizAB)
        return matrizAB
    else:
        return None

i=0
j=0

filas1=int(input("filas matriz 1"))
columnas1=int(input("columnas matriz 1"))

matriz1 = [None] * filas1
for i in range(filas1):
    matriz1[i] = [None] * columnas1

#lectura de la matriz
for i in range(filas1):
    for j in range(columnas1):
        print "elemento M_",i,j
        matriz1[i][j] = float(input())
imprimir_matriz(matriz1)

filas2=int(input("filas matriz 2"))
columnas2=int(input("columnas matriz 2"))

matriz2 = [None] * filas2
for i in range(filas2):
    matriz2[i] = [None] * columnas2

#lectura de la matriz
for i in range(filas2):
    for j in range(columnas2):
        print "elemento M_",i,j
        matriz2[i][j] = float(input())
imprimir_matriz(matriz2)

if (prod_mat(matriz1,matriz2)!=None):
    imprimir_matriz(prod_mat(matriz1,matriz2))
else:
    print "no es posible hacer el producto"
