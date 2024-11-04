from random import randint
import socket
import time

SOCK_BUFFER = 1024


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 5000)

    print(f"Conectando a servidor {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)
    
    for _ in range(10):
        msg = f"{20240001 + randint(0, 200)},{','.join([f'{randint(0, 20)}' for _ in range(14)])}"

        print(f"Enviando notas: {msg}")
        sock.sendall(msg.encode('utf-8'))
        data = sock.recv(SOCK_BUFFER)

        print(f"Recibi: {data}")

        time.sleep(1)

    sock.close()
