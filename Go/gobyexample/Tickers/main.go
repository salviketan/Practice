package main

import (
	"fmt"
	"runtime"
	"time"
)

func main() {
	fmt.Println("Goroutines at start:", runtime.NumGoroutine())

	ticker := time.NewTicker(500 * time.Millisecond)
	done := make(chan bool)

	go func() {
		for {
			select {
			case <-done:
				return
			case t := <-ticker.C:
				fmt.Println("ticker at ", t)
			}
		}
	}()

	time.Sleep(1600 * time.Millisecond)
	ticker.Stop()
	done <- true // comment this line to see Goroutine Leak/Zombie goroutines.
	fmt.Println("Ticker stopped")

	fmt.Println("Goroutines at end:", runtime.NumGoroutine())

}

// NOTE:- runtime.NumGoroutine() - "Use this to print the number of active goroutines in our code.
// We have used this to find out Goroutine Leaks in our code by printing number of active goroutines
// before and after our logic."
