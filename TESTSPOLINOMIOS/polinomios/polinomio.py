# coding: utf8
# Programa que lee un polinomio de grado n y lo evalúa en un valor x

print("Ingrese el grado del polinomio")
n=input()

while not(isinstance(n,int)):
    print("Ingrese n (un número entero):")
    n=input()

coeficientes=[]

print("Ingrese los coeficientes:")

i=0
while i<n+1:
	coeficientes.append(input())
	i=i+1

print(coeficientes)

print "Introduce x "
x=input()
fx=0
i=0
while i<n+1:
	fx=fx+coeficientes[i]*pow(x,i)
	i=i+1

print fx	
	
