import socket

SOCK_BUFFER = 1024


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("localhost", 5000)
    print(f"Conectando a servidor {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    msg = "20240001,1,10,11,11,17,16,19,11,18,17,17,5,3,9"

    sock.sendall(msg.encode('utf-8'))
    data = sock.recv(SOCK_BUFFER)

    sock.close()

    print(f"Recibi: {data}")
