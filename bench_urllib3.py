import urllib3
import sys

CHUNK_SIZE = 16384

def main():
    http = urllib3.PoolManager()
    r = http.request('GET', 'localhost:8080', preload_content=False, decode_content=False)
    while True:
        data = r.read(CHUNK_SIZE)
        if data is None:
            break
        sys.stdout.write(data)


if __name__ == "__main__":
    main()
