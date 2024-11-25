from multiprocessing import Process
import time

num_proc = 64

N = 200_000

def potencia(exponente: int, base: int = N) -> int:
    pot = 1

    for _ in range(exponente):
        pot = pot * base

    return pot


if __name__ == '__main__':
    inicio = time.perf_counter()

    procesos = list()

    for _ in range(num_proc):
        proceso = Process(target=potencia, args=(N // num_proc, ))
        procesos.append(proceso)

    for proceso in procesos:
        proceso.start()
    
    for proceso in procesos:
        proceso.join()

    fin = time.perf_counter()

    t_ejecucion = fin - inicio

    print(f"Tiempo de ejecucion multiproceso con {num_proc} procesos: {t_ejecucion:0.5f} segundos")
