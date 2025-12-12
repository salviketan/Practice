package main

import "fmt"

// pi1 chan<- string :- Meaning of this line is we can send data(in this case "string") to the
// passed channel in func arg
func ping(pi1 chan<- string, msg string) {
	pi1 <- msg
	fmt.Println("pi1:", pi1)
}

// pings <-chan string :- Meaning of this line is we can recieve data(in this case "string") from
// the passed channel in arg
// pongs chan<- string :- Meaning of this line is we can send data(in this case "string") to the
// passed channel in arg
func pong(pi2 <-chan string, po1 chan<- string) {
	fmt.Println("pi2:", pi2)
	fmt.Println("po1:", po1)
	msg := <-pi2
	po1 <- msg
}

func main() {
	pings := make(chan string)
	pongs := make(chan string)
	fmt.Println("pings:", pings)
	fmt.Println("pongs:", pongs)

	go ping(pings, "passed msg")
	go pong(pings, pongs)

	fmt.Println(<-pongs)
	fmt.Println("pongs:", pongs)
}
