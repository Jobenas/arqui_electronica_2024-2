from random import randint


if __name__ == '__main__':
    cabeceras = [f"lab_{idx + 1}" for idx in range(12)]
    cabeceras.append("e1")
    cabeceras.append("e2")
    
    cabeceras_str = ','.join(cabeceras)
    contenido = f"{cabeceras_str}\n"

    notas = [str(randint(1, 20)) for _ in range(len(cabeceras))]
    linea = ','.join(notas)
    contenido += f"{linea}\n"

    with open("notas.csv", "w+") as f:
        f.write(contenido)
    
    print("Termine de escribir el archivo")