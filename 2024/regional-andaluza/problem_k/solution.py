def contar_letras(texto):
    contador = {}
    for letra in texto:
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1
    return contador

def puede_formar_palabra(palabra, dicc_letras):
    dicc_letras_actual = contar_letras(palabra)
    for letra, cantidad in dicc_letras_actual.items():
        if cantidad > dicc_letras.get(letra, 0):
            return False
    return True

def encontrar_palabra_maxima(letras, palabras):
    dicc_letras = contar_letras(letras)
    mejor_palabra = ""

    for palabra in palabras:
        if puede_formar_palabra(palabra, dicc_letras):
            # Seleccionar la palabra más larga o en orden lexicográfico si tienen el mismo tamaño
            if len(palabra) > len(mejor_palabra) or (len(palabra) == len(mejor_palabra) and palabra < mejor_palabra):
                mejor_palabra = palabra

    return mejor_palabra if mejor_palabra else "No es posible"

letras_entrada = input()
num_palabras = int(input())
palabras_entrada = [input().strip() for _ in range(num_palabras)]

resultado = encontrar_palabra_maxima(letras_entrada, palabras_entrada)
print(resultado)