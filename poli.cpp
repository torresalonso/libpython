#include <stdio.h>
#include <iostream>
#include <math.h>
using namespace std;

int main() {

  //declaración de variables.
  double x=0, fx=0;
  int n=0, i=0;

  //leer el grado.
  cout<<"Introduce el grado del polinomio\n";
  cin>>n;

  //declarar el arreglo que almacenará los coeficientes del polinomio.
  double coeficientes[n+1];

  //se leen desde el término independiente hasta el término de mayor potencia
  for(i=0;i<=n;i++){
    cout << "a_" <<i<<"\n";
    cin>>coeficientes[i];
  }

  //leer el valor donde se evaluará el polinomio
  cout<<"Introduce x:\n";
  cin>>x;

  /*Código para evaluar el polinomio. Se recorre el vector de coeficientes y se multiplica cada uno por la respectiva potencia
  de x; el comando pow(<base>,<exponente>);  está definido en la librería math.h */
  for(i=0;i<=n;i++)
    fx+=coeficientes[i] * pow(x,i);


  cout<<"El polinomio evaluado en " << x << " es " << fx<<"\n";


    return 0;
  }
