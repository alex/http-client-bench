try:
    from httplib import HTTPConnection
except ImportError:
    from http.client import HTTPConnection

import sys


CHUNK_SIZE = 16384

def main():
    conn = HTTPConnection('localhost', 8080)
    conn.request('GET', '/')
    r = conn.getresponse()

    while True:
        sys.stdout.write(r.read(CHUNK_SIZE))


if __name__ == "__main__":
    main()

