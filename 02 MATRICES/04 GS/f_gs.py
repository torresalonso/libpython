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

def GS(matriz):
    i = 0
    j = 0
    k = 0
    n = len(matriz)
    escalar = 0
    #Creación de la matriz ortogonal
    Q = [None] * n
    for i in range(n):
        Q[i] = [None] * n
    #q1=v1
    for i in range(n):
        Q[i][0] = matriz[i][0]

    print "Matriz Q:"
    imprimir_matriz(Q)
    time.sleep(3)
    os.system("clear")

    vec_qj = []
    vec_v = []
    comb_lin_qs = []
    for i in range(n):
        comb_lin_qs.append(0)
        vec_qj.append(0)
        vec_v.append(0)
    os.system("clear")

    #--Ortogonalizar el resto de columnas:
    #recorrer las columnas desde la segunda (i=1) hasta la última (i=n-1)
    i = 1
    while i < n:
        #copiar el vector i-ésimo que va a ortogonalizarse en vec_v
        for k in range(n):
            vec_v[k] = matriz[k][i]

        print "Vector a ortogonalizar:"
        print vec_v
        #con el vector copiado, armar la combinación lineal:
        j = 0
        while j < i:
            #copiar el j-ésimo vector ortogonalizado q de la matriz Q
            for k in range(n):
                vec_qj[k] = Q[k][j]

            print "Vector q j-ésimo:"
            print vec_qj

            #hacer el producto interior para construir el escalar:
            escalar = prod_int(vec_v,vec_qj)/prod_int(vec_qj,vec_qj)
            #multiplicar el vector qj por el escalar
            for k in range(n):
                vec_qj[k]*=escalar
            #hacer la combinación lineal
            for k in range(n):
                comb_lin_qs[k] += vec_qj[k]

            #pasar al siguiente vector qj
            j += 1
        #restar al vector v el múltiplo del vector qj
        for k in range(n):
            vec_v[k] -= comb_lin_qs[k]
        #habiendo recorrido todos los vectores q ortogonales, el vector v está ortogonalizado. Lo metemos a la matriz
        for k in range(n):
            Q[k][i] = vec_v[k]
        print "Matriz Q:"
        imprimir_matriz(Q)
        time.sleep(10)
        os.system("clear")
        #pasamos a la siguiente columna para ortogonalizar
        i += 1
        #reiniciar el vector comb_lin_qs
        for k in range(n):
            comb_lin_qs[k]=0
    imprimir_matriz(Q)


i = 0
j = 0
n = int(input("n:"))
#creación de la matriz
matriz = [None] * n
for i in range(n):
    matriz[i] = [None] * n

#lectura de la matriz
for i in range(n):
    for j in range(n):
        print "elemento M_",i,j
        matriz[i][j] = float(input())

imprimir_matriz(matriz)
time.sleep(3)
os.system("clear")

GS(matriz)
