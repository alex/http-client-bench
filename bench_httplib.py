try:
    from httplib import HTTPConnection
except ImportError: # Python 3
    from http.client import HTTPConnection
import sys


CHUNK_SIZE = 16384

def main():
    h1 = HTTPConnection('localhost', 8080)
    a = h1.request('GET', '/')
    r = h1.getresponse()

    while True:
        sys.stdout.write(r.read(CHUNK_SIZE))


if __name__ == "__main__":
    main()

