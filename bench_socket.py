import socket
import sys


CHUNK_SIZE = 16384

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 8080))
    s.sendall(b"GET / HTTP/1.1\r\n\r\n")
    while True:
        sys.stdout.write(s.recv(CHUNK_SIZE))


if __name__ == "__main__":
    main()
