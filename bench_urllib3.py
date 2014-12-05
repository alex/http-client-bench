import sys

import urllib3


CHUNK_SIZE = 16384

def main():
    http = urllib3.PoolManager()
    r = http.request(
        'GET', 'localhost:8080', preload_content=False, decode_content=False
    )
    while True:
        sys.stdout.write(r.read(CHUNK_SIZE))


if __name__ == "__main__":
    main()
