#include <iostream>
// #include <unordered_map> // Ya no es necesario si usas array
#include <string>
#include <vector> // Para el array de hijos si prefieres vector, o usa array C-style/std::array
#include <array>  // Mejor opción para tamaño fijo

using namespace std;

const int ALPHABET_SIZE = 10; // Para dígitos '0' a '9'

class TrieNode {
public:
    // Usa un array en lugar de un map. std::array es más seguro.
    array<TrieNode*, ALPHABET_SIZE> children;
    int count; // Cuenta cuántas palabras pasan por este nodo

    TrieNode() : count(0) {
        // Inicializa todos los punteros hijos a nullptr
        children.fill(nullptr);
    }

    // **Importante: Añadir un destructor para liberar memoria**
    ~TrieNode() {
        for (int i = 0; i < ALPHABET_SIZE; ++i) {
            delete children[i]; // Esto llamará recursivamente a los destructores hijos
        }
    }
};

class Trie {
private:
    TrieNode* root;

public:
    Trie() {
        root = new TrieNode();
    }

    // **Importante: Añadir un destructor para el Trie**
    ~Trie() {
        delete root; // Esto iniciará la cadena de deleción recursiva
    }


    void insert(const string& number) {
        TrieNode* node = root;
        for (char digit : number) {
            // Asume que digit es un carácter entre '0' y '9'
            int index = digit - '0';

            // Valida el índice si es necesario (depende de las restricciones del problema)
            if (index < 0 || index >= ALPHABET_SIZE) {
                 // Decide cómo manejar caracteres inválidos: ignorar, error, etc.
                 // Por ahora, asumimos que la entrada es válida.
                 continue;
            }

            if (node->children[index] == nullptr) {
                node->children[index] = new TrieNode();
            }
            node = node->children[index];
            node->count++; // Incrementa el contador en cada nodo del camino
        }
    }

    int countPrefix(const string& prefix) {
        TrieNode* node = root;
        for (char digit : prefix) {
            int index = digit - '0';

            if (index < 0 || index >= ALPHABET_SIZE) {
                // Prefijo contiene carácter inválido
                return 0;
            }

            if (node->children[index] == nullptr) {
                // El prefijo no existe en el Trie
                return 0;
            }
            node = node->children[index];
        }
        // Al final del prefijo, node apunta al último nodo del prefijo.
        // Su contador 'count' tiene el número de palabras insertadas que tienen este prefijo.
        return node->count;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    int caseNum = 1;
    string line; // Para leer líneas completas si es necesario

    // Lee N y Q primero. Ajusta según el formato exacto.
    // Si N y Q están en la misma línea:
    while (cin >> N >> Q) {
        // Consume el salto de línea restante después de leer N y Q
        getline(cin, line);

        Trie trie; // Crea un nuevo Trie para cada caso de prueba

        for (int i = 0; i < N; ++i) {
            getline(cin, line); // Lee el número como string
            if (!line.empty()) { // Evita procesar líneas vacías si es posible
               trie.insert(line);
            }
        }

        cout << "Case " << caseNum++ << ":\n"; // Formato de salida
        for (int i = 0; i < Q; ++i) {
            getline(cin, line); // Lee el prefijo como string
             if (!line.empty()) {
                cout << trie.countPrefix(line) << "\n";
             } else {
                 // Decide qué hacer con un prefijo vacío.
                 // Tal vez debería devolver N? O 0?
                 // El código actual devuelve 0 porque el bucle no se ejecuta.
                 // Si un prefijo vacío debe contar todas las palabras, necesitas
                 // almacenar N o devolver root->count (si root->count se mantuviera correctamente).
                 // La implementación actual devuelve 0 para prefijo vacío.
                 cout << 0 << "\n";
             }
        }
         // El bucle while(cin >> N >> Q) manejará múltiples casos de prueba
         // hasta que la entrada falle (EOF).
    }


    return 0;
}