package main

import (
	"net/http"
)

var CHUNK = [1024]byte{}

type FastStreamHandler struct{}

func (f FastStreamHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	w.Header().Add("Content-Type", "application/octet-stream")
	for {
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
