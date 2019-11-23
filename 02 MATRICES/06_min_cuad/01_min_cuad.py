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

def reduccion_GJ(matriz_aux):
    i=0
    j=0

    reng_pivote = 0
    col_pivote = 0
    filas = len(matriz_aux)
    while reng_pivote < filas:
        pivote = matriz_aux[reng_pivote][col_pivote]

        #si el pivote es 0, intercambiar renglón
        if(pivote == 0):
            intercambiar_rengones(matriz_aux, reng_pivote,col_pivote)
            pivote = matriz_aux[reng_pivote][col_pivote]

        #convertir el pivote en 1
        if(pivote != 1):
            multiplo_escalar(matriz_aux, reng_pivote,1/pivote)
            pivote = matriz_aux[reng_pivote][col_pivote]

        #convertir los elementos bajo el pivote en 0
        for i in range(reng_pivote+1,filas):
            if(matriz_aux[i][col_pivote]!=0):
                sumar_multiplo_renglon(matriz_aux,reng_pivote,i,-(matriz_aux[i][col_pivote]/pivote))

        #convertir los elementos sobre el pivote en 0
        for i in range(reng_pivote - 1,-1,-1):
            if(matriz_aux[i][col_pivote]!=0):
                sumar_multiplo_renglon(matriz_aux,reng_pivote,i,-(matriz_aux[i][col_pivote]/pivote))

        reng_pivote += 1
        col_pivote += 1
    return matriz_aux


#################################### Bloque de código que se ejecuta

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
time.sleep(2)

grado = int(input("Grado del polinomio"))
matriz_aux = [None] * (grado+1)
for i in range(grado+1):
    matriz_aux[i] = [None] * (grado+2)

suma = 0

#calcular las sumas y armar la matriz de coeficientes
for i in range (len(matriz_aux)):
    for j in range(len(matriz_aux)):
        for k in range(n):
            suma += datos_x[k]**(i+j)
        matriz_aux[i][j]=suma
        suma = 0
suma = 0

for i in range(len(matriz_aux)):
    for k in range(n):
        suma += datos_y[k]*(datos_x[k]**(i))
    matriz_aux[i][grado+1] = suma
    suma=0

print "Sistema de ecuaciones para ajustar la parábola:"
imprimir_matriz(matriz_aux)

reduccion_GJ(matriz_aux)
time.sleep(3)
imprimir_matriz(matriz_aux)


#cálculo del error estándar:
#sr:
suma=0
#for i in range(n):
	#suma += (datos_y[i]-a_0-a_1*datos_x[i])**2
#error_estandar = math.sqrt(suma/(n-2))
#print "el error estándar es ",error_estandar
