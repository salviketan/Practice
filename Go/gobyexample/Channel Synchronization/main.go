package main

import (
	"fmt"
	"time"
)

func worker(done chan bool) {
	fmt.Print("Working...")
	time.Sleep(time.Duration(3) * time.Second)
	fmt.Println("done")
	done <- true
}

func main() {
	t0 := time.Now()
	done := make(chan bool, 1)

	// worker(done)
	go worker(done)

	fmt.Println("before blocking receive")

	<-done

	fmt.Println("after blocking receive")
	fmt.Println(time.Since(t0))
}
