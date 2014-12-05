package main

import (
	"io"
	"net/http"
	"os"
)

func main() {
	response, _ := http.Get("http://localhost:8080")
	io.Copy(os.Stdout, response.Body)
}
