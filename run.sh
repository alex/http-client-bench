#!/usr/bin/env bash

export BENCH_SIZE="$((1024 * 1024 * 1024))"

echo "BENCH SOCKET:"
python bench_socket.py | pv --stop-at-size --size=${BENCH_SIZE} > /dev/null
echo "BENCH HTTPLIB:"
python bench_httplib.py | pv --stop-at-size --size=${BENCH_SIZE} > /dev/null
echo "BENCH URLLIB3:"
python bench_urllib3.py | pv --stop-at-size --size=${BENCH_SIZE} > /dev/null
echo "BENCH REQUESTS"
python bench_requests.py | pv --stop-at-size --size=${BENCH_SIZE} > /dev/null
echo "BENCH GO HTTP"
go run bench_http.go | pv --stop-at-size --size=${BENCH_SIZE} > /dev/null
