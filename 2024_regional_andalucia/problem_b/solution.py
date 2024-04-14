def encontrar_bloqueadores_minimos(personajes):

    # Agregar nombre al trie
    def agregar_al_trie(trie, nombre):
        actual = trie
        for letra in nombre:
            if letra not in actual:
                actual[letra] = {}
            actual = actual[letra]

    # Verificar si un prefijo está en el trie
    def es_prefijo_en_trie(trie, prefijo):
        actual = trie
        for letra in prefijo:
            if letra in actual:
                actual = actual[letra]
            else:
                return False
        return True
    
    trie_buenos = {}
    nombres_malos = []

    for personaje in personajes:
        signo = personaje[0]
        nombre = personaje[1:]
        if signo == '+':
            agregar_al_trie(trie_buenos, nombre)
        else:
            nombres_malos.append(nombre)

    bloqueadores = set()

    # Para cada nombre malo buscar el prefijo más corto que no esté en el trie de buenos
    for malo in nombres_malos:
        encontrado = False
        for i in range(1, len(malo) + 1):
            prefijo = malo[:i]
            if not es_prefijo_en_trie(trie_buenos, prefijo):
                bloqueadores.add(prefijo)
                encontrado = True
                break
        if not encontrado:
            print("-1")  # Devuelve -1 si no se encuentra un bloqueador adecuado
            return

    bloqueadores = list(bloqueadores)
    bloqueadores = sorted(bloqueadores)

    print(len(bloqueadores))
    for prefijo in bloqueadores:
        print(prefijo)


n = int(input())
personajes = []
for _ in range(n):
    personajes.append(input().strip())

encontrar_bloqueadores_minimos(personajes)