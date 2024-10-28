from random import randint


if __name__ == '__main__':  
    cabeceras_str = f"codigo,{','.join([f"lab_{idx + 1}" for idx in range(12)])},e1,e2"
    contenido = f"{cabeceras_str}\n"
    codigo_base = 20240001

    for idx in range(100):
        linea = f"{codigo_base + idx},{','.join([f"{randint(1, 20)}" for _ in range(14)])}"
        contenido += f"{linea}\n"

    with open("notas.csv", "w+") as f:
        f.write(contenido)
    
    print("Termine de escribir el archivo")