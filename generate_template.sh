#!/bin/bash

# Verifica argumentos
if [ $# -ne 2 ]; then
  echo "Uso: $0 <directorio_base> <numero_de_letras>"
  exit 1
fi

BASE_DIR="$1"
NUM_LETTERS="$2"

# Validar que NUM_LETTERS sea un número entre 1 y 26
if ! [[ "$NUM_LETTERS" =~ ^[0-9]+$ ]] || [ "$NUM_LETTERS" -lt 1 ] || [ "$NUM_LETTERS" -gt 26 ]; then
  echo "Error: el número de letras debe estar entre 1 y 26"
  exit 1
fi

mkdir -p "$BASE_DIR"

# Generar directorios
for ((i=0; i<NUM_LETTERS; i++)); do
  # Convertir índice a letra (ASCII: A=65)
  letter=$(printf "\\$(printf '%03o' $((65 + i)))")
  
  FULL_PATH="$BASE_DIR/$letter"
  
  mkdir -p "$FULL_PATH/code" "$FULL_PATH/samples" "$FULL_PATH/testcases"
  touch "$FULL_PATH/statement.md"
done

echo "Estructura creada en $BASE_DIR con $NUM_LETTERS letras"