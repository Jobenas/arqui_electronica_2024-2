import time
from threading import Thread

N = 70_000_000


def cuenta(n: int):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    inicio = time.perf_counter()
    t1 = Thread(target=cuenta, args=(N // 2,))
    t2 = Thread(target=cuenta, args=(N // 2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    fin = time.perf_counter()

    t_ejecucion = fin - inicio

    print(f"Tiempo de ejecucion: {t_ejecucion:0.5f} segundos")
