package main

import "fmt"

// Channels:- Hold Data, Thread Safe, Listen for Data/

func deadlockOutput_main() {
	var c = make(chan int)
	c <- 1 // '<-':- used to add the value to the channel
	fmt.Println(c)
	var i = <-c //This line is used to retrive the value in channel to var 'i'. after this channel becomes empty
	fmt.Printf("c: %v, i: %v", c, i)
}

// This is how channel should be used.
func main() {
	var c = make(chan int)
	go process(c)
	fmt.Println(c)
	fmt.Println(<-c)
}

func process(c chan int) {
	c <- 123
}
