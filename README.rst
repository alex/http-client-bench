HTTP Client Benchmarks
======================

To start the server::

    $ go run server.go

And in a second shell (run each until the data stabilizes)::

    $ python bench_socket.py | pv > /dev/null
    $ python bench_requests.py | pv > /dev/null
    $ python bench_urllib3.py | pv > /dev/null
    $ go run bench_http.go | pv > /dev/null
