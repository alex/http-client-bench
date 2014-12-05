package main

import (
	"net/http"
	"strconv"
)

// 32 GiB
var DESIRED_SIZE = 1024 * 1024 * 1024 * 32
var CHUNK = [1024]byte{}

type FastStreamHandler struct{}

func (f FastStreamHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	w.Header().Add("Content-Type", "application/octet-stream")
	w.Header().Add("Content-Length", strconv.Itoa(DESIRED_SIZE))
	for i := 0; i < DESIRED_SIZE/len(CHUNK); i++ {
		_, err := w.Write(CHUNK[:])
		if err != nil {
			break
		}
	}
}

func main() {
	server := http.Server{
		Addr:    ":8080",
		Handler: FastStreamHandler{},
	}
	server.ListenAndServe()
}
