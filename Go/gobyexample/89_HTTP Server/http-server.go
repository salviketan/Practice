package main

import (
	"fmt"
	"net/http"
)


func hello(w http.ResponseWriter, req *http.Request)  {

	fmt.Fprintf(w, "hello\n")
}

func handler(w http.ResponseWriter, req *http.Request)  {
	
	for name, header := range req.Header {
		for _, h := range header {
			fmt.Fprintf(w, "%v: %v\n", name, h)
		}
	}
}


func main()  {
	
	http.HandleFunc("/hello", hello)
	http.HandleFunc("/header", handler)

	http.ListenAndServe(":8090", nil)
}