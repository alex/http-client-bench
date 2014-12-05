import sys

import requests


CHUNK_SIZE = 16384

def main():
    r = requests.get("http://localhost:8080", stream=True)
    for chunk in r.iter_content(CHUNK_SIZE):
        sys.stdout.write(chunk)


if __name__ == "__main__":
    main()
