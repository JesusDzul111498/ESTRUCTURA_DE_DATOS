#include <iostream>
#include "include/NATURAL.h"
using namespace std;


void print_options();

int main(){

    NATURAL number;
    int n,op,x1;

    do{
    cout << "\n(-1 para salir del programa)\nenter a number: "; cin >> n; number.Setx(n);
    cout << "What would I like to do with that number?\n" ;// QUE QUISIERA HACER CON ESE NUMERO?
    print_options();cin >> op;
            switch (op){
            case 1:
                cout << "\n1.- Verificar si es 0"<<endl;
                if(number.veri()==1){
                    cout << "\nEL " <<n<<" numero es igual a 0\n";}else{
                        cout << "\nEL "<<n<<" numero es diferente a 0\n";
                    }
                break;
            case 2:
                cout << "\n2.-Sucesor"<<endl;
                cout << "\nEl sucecero de " <<n<<" es: "<< number.suce();
                break;
            case 3:
                cout << "\n3.-Es 0"<<endl;
                cout << "\El numero "<<n<<" ahora es " << number.zero();
                break;
            case 4:
                cout << "\n4.-Igual"<<endl;
                cout << "El numero "<<n<<" es igual a "<<n;
                break;
            case 5:
                cout << "\n5.-Suma"<<endl;
                cout << "\nIngresa el numero que le quieres sumar: ";cin >> x1; number.Setc(x1);
                cout << "La suma del numero "<<n<<" con el numero "<<x1<<" es: "<< number.suma(n,x1);
                break;
            case 6:
                cout << "\n6.-Antecesor"<<endl;
                cout << "El numero antecesor a "<<n<<" es: "<<number.ante();
                break;
            case 7:
                cout << "\n7.-Diferencia "<<endl;
                 cout << "Ingrese un numero mas, para determinar cual es la diferencia\n";
                cout << "numero: "; cin >> x1; number.Setc(x1);
                cout << "\nLa diferencia entre "<<n<<" y "<<x1<<" es: " << number.dif(n,x1);
                break;
            case 8:
                cout << "\n8.-Menor"<<endl;
                cout << "Ingrese un numero mas, para determinar cual es el menor\n";
                cout << "numero: "; cin >> x1; number.Setc(x1);
                cout << "\nEl numero menor entre "<< n <<" y "<< x1 <<" es: " << number.menor();
                break;
                cout << "Escoja un numero entre el rango 1 y 8"<<endl;
            default:
                cout << "\nIngrese un numero de 1-8\n";
                break;
             }
    }while(n != -1);

    return 0;
}

void print_options(){
    cout << "*****Choose an option***** " <<endl;//ELIJA UNA OPCION
    cout << "1.- Verificar si es 0"<<endl;
    cout << "2.-Sucesor"<<endl;
    cout << "3.-Es 0"<<endl;
    cout << "4.-Igual"<<endl;
    cout << "5.-Suma"<<endl;
    cout << "6.-Antecesor"<<endl;
    cout << "7.-Diferencia "<<endl;
    cout << "8.-Menor"<<endl;
    cout << "Choose an option: ";

}
