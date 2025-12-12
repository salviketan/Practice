package main

import "fmt"

var messages2 = make(chan string, 2)

func b() { messages2 <- "b string" }

func main() {

	messages1 := make(chan string, 2)

	messages1 <- "buffered"
	messages1 <- "channel"

	fmt.Println(<-messages1)
	fmt.Println(<-messages1)

	// My code
	go func() { messages2 <- "a string" }()

	go b()

	a := <-messages2

	b := <-messages2

	fmt.Println(a)
	fmt.Println(b)
}
