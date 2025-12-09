package main

import "fmt"

var message = make(chan string, 2)

func b() { message <- "b string" }

func main() {

	go func() { message <- "a string" }()

	go b()

	a := <-message

	b := <-message

	fmt.Println(a)
	fmt.Println(b)
}
