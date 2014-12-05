try:
    from httplib import HTTPConnection
except ImportError:
    from http.client import HTTPConnection

import signal
import sys


CHUNK_SIZE = 16384

def main():
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)

    conn = HTTPConnection('localhost', 8080)
    conn.request('GET', '/')
    r = conn.getresponse(buffering=True)

    while True:
        sys.stdout.write(r.read(CHUNK_SIZE))


if __name__ == "__main__":
    main()

