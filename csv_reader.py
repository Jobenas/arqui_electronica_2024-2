

if __name__ == '__main__':
    with open("notas.csv", "r") as f:
        contenido = f.read()

    filas = contenido.split("\n")

    for fila in filas:
        elementos = fila.split(",")
        print(elementos)