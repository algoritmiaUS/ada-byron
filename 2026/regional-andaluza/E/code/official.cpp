#include <iostream>
#include <vector>
#include <cmath>

using namespace std;
int mayorNumeroPosible(int n);
int menorNumeroPosible(int n);
void ordenar(vector<int> &v);

int main(int argc, char **argv)
{
	int numero, mayor, menor;
	int contador = 0;
	int diferencia = 0;
	std::cin >> numero;
	if (!std::cin)
	{
	    std::cerr << "Error de lectura" << std::endl;
	    return -1;
	}

		while (diferencia != 6174)
		{
			mayor = mayorNumeroPosible(numero);
			menor = menorNumeroPosible(numero);
			diferencia = mayor - menor;
			numero = diferencia;
			if (diferencia == 0)
				break;
			contador++;
		}
	std::cout << contador << std::endl;
	return 0;
}

int mayorNumeroPosible(int n)
{
	std::vector <int> v;
	int cociente, resto, mayor = 0;
	for (int i = 3; i >= 0; i--)
	{
		cociente = n/(int)pow(10, i);
		resto = n%(int)pow(10, i);
		n = resto;
		v.push_back(cociente);
	}
	ordenar(v);

	for (int i = 3; i >= 0; i--)
	{
		mayor += (int)pow(10, 3-i) * v[i];
	}

	return mayor;
}

int menorNumeroPosible(int n)
{
	std::vector <int> v;
	int cociente, resto, menor = 0;
	for (int i = 3; i >= 0; i--)
	{
		cociente = n/(int)pow(10, i);
		resto = n%(int)pow(10, i);
		n = resto;
		v.push_back(cociente);
	}
	ordenar(v);

	for (int i = 3; i >= 0;i--)
	{
		menor += (int)pow(10, i) * v[i];
	}

	return menor;
}


void ordenar(vector<int> &v)
{
    int aux;
    size_t posMax;

    for(size_t i = 0; i < v.size() -1; i++)
    {
        posMax = i;
        for(size_t j = i+1; j < v.size(); j++)
        {
            if (v[j] > v[posMax])
                posMax = j;
        }
        aux = v[posMax];
        v[posMax] = v[i];
        v[i] = aux;
    }
}
