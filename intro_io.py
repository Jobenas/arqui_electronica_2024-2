import time


print("Este es un print fuera del if __name__")

def suma(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    inicio = time.perf_counter()
    a = 3
    b = 4
    c = suma(a, b)
    string_salida = f"El resultado es {c}"
    inicio_print = time.perf_counter()
    print(string_salida)
    fin = time.perf_counter()

    print(f"resultados -> \n\t\tTiempo de print: {fin - inicio_print} segundos\n\t\tTiempo total: {fin - inicio} segundos\n\t\tPorcentaje de operacion E/S: {((fin - inicio_print)/(fin - inicio))*100}%")
