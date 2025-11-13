package main

import (
	"fmt"
	"math/rand"
	"time"
)

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
	fmt.Println("The unbuffer channel 1")
	unbufferChannel1()
	fmt.Println("The unbuffer channel 2")
	unbufferChannel2()
	fmt.Println("The buffer channel")
	bufferChannel()

	fmt.Println("some what realistic")
	someWhatRealisticFunc()
}

func someWhatRealisticFunc() {
	var MAX_CHICKEN_PRICE float32 = 5.0
	var chickenChannel = make(chan string)
	var website = []string{"Dmart.com", "walmart.com", "wholefoods.com"}
	for i := range website {
		go checkChickenPrice(website[i], chickenChannel, MAX_CHICKEN_PRICE)
	}
	sendMessage(chickenChannel)

}

func checkChickenPrice(website string, chickenChannel chan string, MAX_CHICKEN_PRICE float32) {
	for {
		time.Sleep(time.Second * 1)
		var chickenPrice = rand.Float32() * 20
		if MAX_CHICKEN_PRICE <= chickenPrice {
			chickenChannel <- website
		}
	}
}

func sendMessage(chickenChannel chan string) {
	fmt.Printf("\nFound a deal on chicken at %s", <-chickenChannel)
}

func unbufferChannel1() {
	var uc1 = make(chan int)
	go unbufferProcess1(uc1)
	println(<-uc1)

}

func unbufferProcess1(uc1 chan int) {
	uc1 <- 123
}

func unbufferChannel2() {
	var uc2 = make(chan int)
	go unbufferProcess2(uc2)
	for i := range uc2 {
		println(i)
	}

}

func unbufferProcess2(uc2 chan int) {
	defer close(uc2)
	for i := 0; i <= 5; i++ {
		uc2 <- i
	}
}

func bufferChannel() {
	var bc = make(chan int, 5)
	go bufferProcess(bc)
	for i := range bc {
		time.Sleep(time.Second * 1)
		println(i)
	}

}

func bufferProcess(bc chan int) {
	defer close(bc)
	for i := 0; i <= 5; i++ {
		bc <- i
	}
	fmt.Println("Exiting process")
}
