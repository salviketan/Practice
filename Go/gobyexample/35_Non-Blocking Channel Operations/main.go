package main

import (
	"fmt"
)

func main() {
	message := make(chan string)
	signal := make(chan string)

	select {
	case msg := <-message:
		fmt.Println("received message", msg)
	default:
		fmt.Println("No message received")
	}

	msg := "foobar"
	select {
	case message <- msg:
		fmt.Println("sent message", msg)
	default:
		fmt.Println("No message sent")
	}

	select {
	case msg := <-message:
		fmt.Println("received message", msg)
	case sig := <-signal:
		fmt.Println("received  signal", sig)
	default:
		fmt.Println("Nothing sent, so nothing received")
	}
}
