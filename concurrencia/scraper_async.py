import asyncio
import time

import aiohttp


async def download_site(url: str, session: aiohttp.ClientSession) -> None:
    async with session.get(url) as response:
        # print(f"Lei de {url}")
        pass


async def download_all_sites(sites: list[str]) -> None:
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*(download_site(url, session) for url in sites))

if __name__ == '__main__':
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 160

    inicio = time.perf_counter()
    asyncio.run(download_all_sites(sites))
    fin = time.perf_counter()

    t_ejecucion = fin - inicio

    print(f"Tiempo de ejecucion asincrono: {fin - inicio} segundos")
