#coding: utf8
import os
import time
import math

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

datos_x = []
datos_y = []

n = int(input("Cantidad de puntos"))

for i in range(n):
	print "Valor de x",i
	datos_x.append(float(input()))
	print "Valor de y",i
	datos_y.append(float(input()))
	os.system("clear")

print "Valores de x:"
imprimir_matriz(datos_x)
print "Valores de y:"
imprimir_matriz(datos_y)
time.sleep(3)
os.system("clear")

a_1 =0
suma = 0
numerador = 0
denominador = 0
sumax = 0
sumay = 0

#El valor de a_1 se va a calcular siguiendo la fórmula:
#n(sumxy)-(sumx)(sumy)
#------------------------
#n(sumxcuad)-(sumx)²

#numerador:
#se calcula primero (sumxy)
for i in range(n):
	suma += datos_x[i]*datos_y[i]
#se multiplica esa suma por n: n(sumxy)
numerador = n*suma;
#se calcula sumx
for i in range(n):
	sumax += datos_x[i]
#se calcula sumy
for i in range(n):
	sumay += datos_y[i]
#se recalcula el numerador n(sumxy)-(sumx)(sumy)
numerador -= sumax*sumay

#denominador:
#se calcula primero (sumxcuad)
suma=0
for i in range(n):
	suma += datos_x[i]**2

#n(sumxcuad)-(sumx)²
denominador = n*suma-sumax**2

a_1 = numerador/denominador

#El valor de a_0 se va a calcular siguiendo la fórmula siguiente.
#(promedio y) -(a_1)(promedio x)
a_0 = (sumay/n)-a_1*(sumax/n)

print "la recta de regresión es ",a_0,"+",a_1,"x"

#cálculo del error estándar:
#sr:
suma=0
for i in range(n):
	suma += (datos_y[i]-a_0-a_1*datos_x[i])**2
error_estandar = math.sqrt(suma/(n-2))
print "el error estándar es ",error_estandar

#cálculo del coeficiente de correlación:
#cálculo del término (sumycuad)
suma=0
for i in range(n):
	suma += datos_y[i]**2
	
#sr:
r = numerador/(math.sqrt(denominador)*math.sqrt(n*suma-sumay**2))
print "el coeficiente de correlación es  ", r
