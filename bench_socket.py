import socket
import sys


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 8080))
    s.sendall(b"GET / HTTP/1.1\r\n\r\n")
    while True:
        sys.stdout.write(s.recv(16384))


if __name__ == "__main__":
    main()
