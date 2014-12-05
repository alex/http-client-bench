package main

import (
	"net/http"
	"strconv"
)

var CHUNK = [1024]byte{}

type FastStreamHandler struct{}

func (f FastStreamHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	size := r.URL.Query().Get("size")
	w.Header().Add("Content-Type", "application/octet-stream")
	if size != "" {
		responseSize, _ := strconv.Atoi(size)
		for i := 0; i < responseSize/len(CHUNK); i++ {
			w.Write(CHUNK[:])
		}
	} else {
		for {
			w.Write(CHUNK[:])
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
