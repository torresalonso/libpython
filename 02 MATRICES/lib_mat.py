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

###################### Operaciones elementales
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
    #Apartar el renglón que se va a intercambiar
    renglon_aux=[]
    for j in range(len(matriz_aux[0])):
        renglon_aux.append(matriz[renglon_a_intercambiar][j])

    #intercambiar los renglones
    for j in range(len(matriz_aux[0])):
        matriz_aux[renglon_a_intercambiar][j] = matriz_aux[reng_pivote][j]
        matriz_aux[reng_pivote][j] = renglon_aux[j]

    return matriz_aux

###################### Reducciones matriciales
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

#Aplica la reducción gaussiana a una matriz rectangular convirtiendo los pivotes en 1.
def reduccion_gaussiana(matriz_aux):
    i=0
    j=0

    reng_pivote = 0
    col_pivote = 0
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

        reng_pivote += 1
        col_pivote += 1
    return matriz_aux

#Aplica el algoritmo Gauss Jordan a una matriz rectangular
def reduccion_GJ(matriz_aux):
    i=0
    j=0

    reng_pivote = 0
    col_pivote = 0

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
###################### Determinante
def determinante(matriz_aux):
    if(len(matriz_aux) != len(matriz_aux[0])):
        return None
    else:
        det=1
        i = 0
        matriz_aux = convertir_triangular(matriz_aux)
        for i in range(len(matriz_aux)):
            det*=matriz_aux[i][i]
        return det




###################### Vectores ortonormales.
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
