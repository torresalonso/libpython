def cotas_raices(grado, polinomio, inf_sup=1):
	cota=0
	polinomio_Q=[]
	negativo=0
	k=0

	#si se pide cota inferior, calcula P(-x):
	if(inf_sup==0):
		for k in range(1, grado+1,2): 
			polinomio[k]*=(-1)

		print polinomio
	print "el valor del coeficiente a_n es: "
	print polinomio[grado];
	
	#si el polinomio tiene como coeficiente a_n<0, multiplicamos por -1 para que funcione el teorema
	if(polinomio[grado]<0):
		for k in range (0,grado+1):
			polinomio[k]=-polinomio[k];
		print polinomio

	



grado=input("grado")
coeficientes=[]
i=0
while (i<grado+1):
	coeficientes.append(input("Coeficiente "))
	i+=1

print coeficientes

print "el polinomio P(-x):"
cotas_raices(grado, coeficientes, 1)

