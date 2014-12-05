import sys

import requests


def main():
    r = requests.get("http://localhost:8080", stream=True)
    for chunk in r.iter_content(16384):
        sys.stdout.write(chunk)


if __name__ == "__main__":
    main()
