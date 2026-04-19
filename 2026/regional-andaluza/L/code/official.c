#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_N 10005
#define MAX_MOTIVOS 100
#define MAX_LEN_MOTIVO 105
#define MAX_OCURRENCIAS (MAX_N * MAX_MOTIVOS)

char adn[MAX_N];
char motivos[MAX_MOTIVOS][MAX_LEN_MOTIVO];
int num_motivos, k;

/* Cada ocurrencia se guarda en 3 arrays paralelos */
int ocurr_fin[MAX_OCURRENCIAS];
int ocurr_ini[MAX_OCURRENCIAS];
int ocurr_id[MAX_OCURRENCIAS];
int num_ocurrencias = 0;

void leer_entrada() {
    fgets(adn, MAX_N, stdin);
    adn[strcspn(adn, "\r\n")] = 0;

    char linea_motivos[MAX_N];
    fgets(linea_motivos, MAX_N, stdin);
    linea_motivos[strcspn(linea_motivos, "\r\n")] = 0;

    char* token = strtok(linea_motivos, " ");
    num_motivos = 0;
    while (token != NULL) {
        strcpy(motivos[num_motivos], token);
        num_motivos++;
        token = strtok(NULL, " ");
    }

    scanf("%d", &k);
}

void eliminar_motivos_duplicados() {
    char unicos[MAX_MOTIVOS][MAX_LEN_MOTIVO];
    int num_unicos = 0;
    int repetido;

    for (int i = 0; i < num_motivos; i++) {
        repetido = 0;
        for (int j = 0; j < num_unicos; j++) {
            if (strcmp(motivos[i], unicos[j]) == 0) {
                repetido = 1;
                break;
            }
        }
        if (!repetido) {
            strcpy(unicos[num_unicos], motivos[i]);
            num_unicos++;
        }
    }

    for (int i = 0; i < num_unicos; i++) {
        strcpy(motivos[i], unicos[i]);
    }
    num_motivos = num_unicos;
}

void buscar_ocurrencias() {
    int n = strlen(adn);
    num_ocurrencias = 0;

    for (int i = 0; i < num_motivos; i++) {
        int len_motivo = strlen(motivos[i]);

        for (int pos = 0; pos <= n - len_motivo; pos++) {
            if (strncmp(adn + pos, motivos[i], len_motivo) == 0) {
                ocurr_ini[num_ocurrencias] = pos;
                ocurr_fin[num_ocurrencias] = pos + len_motivo - 1;
                ocurr_id[num_ocurrencias] = i;
                num_ocurrencias++;
            }
        }
    }
}

void ordenar_ocurrencias_por_fin() {
    for (int i = 0; i < num_ocurrencias - 1; i++) {
        for (int j = i + 1; j < num_ocurrencias; j++) {
            if (ocurr_fin[j] < ocurr_fin[i] ||
               (ocurr_fin[j] == ocurr_fin[i] && ocurr_ini[j] < ocurr_ini[i])) {

                int aux;

                aux = ocurr_fin[i];
                ocurr_fin[i] = ocurr_fin[j];
                ocurr_fin[j] = aux;

                aux = ocurr_ini[i];
                ocurr_ini[i] = ocurr_ini[j];
                ocurr_ini[j] = aux;

                aux = ocurr_id[i];
                ocurr_id[i] = ocurr_id[j];
                ocurr_id[j] = aux;
            }
        }
    }
}

void ordenar_descendente(int v[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (v[j] > v[i]) {
                int aux = v[i];
                v[i] = v[j];
                v[j] = aux;
            }
        }
    }
}

int calcular_minima_longitud() {
    int latest_start[MAX_MOTIVOS];
    int activos[MAX_MOTIVOS];
    int ans = MAX_N + 1;

    for (int i = 0; i < num_motivos; i++) {
        latest_start[i] = -1;
    }

    for (int t = 0; t < num_ocurrencias; t++) {
        int r = ocurr_fin[t];
        int l = ocurr_ini[t];
        int id = ocurr_id[t];

        if (l > latest_start[id]) {
            latest_start[id] = l;
        }

        int num_activos = 0;
        for (int i = 0; i < num_motivos; i++) {
            if (latest_start[i] != -1) {
                activos[num_activos] = latest_start[i];
                num_activos++;
            }
        }

        if (num_activos >= k) {
            ordenar_descendente(activos, num_activos);

            int L = activos[k - 1];
            int longitud = r - L + 1;

            if (longitud < ans) {
                ans = longitud;
            }
        }
    }

    if (ans == MAX_N + 1) {
        return 0;
    }
    return ans;
}

int main() {
    leer_entrada();
    eliminar_motivos_duplicados();

    if (k > num_motivos) {
        printf("0\n");
        return 0;
    }

    buscar_ocurrencias();

    if (num_ocurrencias == 0) {
        printf("0\n");
        return 0;
    }

    ordenar_ocurrencias_por_fin();

    printf("%d\n", calcular_minima_longitud());
    return 0;
}