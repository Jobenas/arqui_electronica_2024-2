from multiprocessing import cpu_count, Pool
import time

import requests

session = None

def set_global_session():
    global session
    if session is None:
        session = requests.session()
    

def download_site(url: str) -> None:
    with session.get(url) as response:
        # print(f"Lei {len(response.content)} bytes de {url}")
        pass


def download_all_sites(sites: list[str]) -> None:
    with Pool(processes=cpu_count(), initializer=set_global_session) as pool:
        pool.map(download_site, sites)


if __name__ == '__main__':
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 160

    inicio = time.perf_counter()
    download_all_sites(sites)
    fin = time.perf_counter()

    t_ejecucion = fin - inicio

    print(f"Tiempo de ejecucion multiproceso: {fin - inicio} segundos")
