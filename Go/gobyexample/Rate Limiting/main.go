package main

import (
	"fmt"
	"time"
)

func main() {
	requests := make(chan int, 5)

	for i := 1; i <= 5; i++ {
		requests <- i
	}
	close(requests)

	limiter := time.Tick(200 * time.Millisecond)

	for req := range requests {
		<-limiter
		fmt.Println("request", req, time.Now())
	}

	burstyLimiter := make(chan time.Time, 3)

	fmt.Println()

	for range 3 {
		burstyLimiter <- time.Now()
	}

	go func() {
		for t := range time.Tick(200 * time.Millisecond) {
			burstyLimiter <- t
		}
	}()

	burstyRequests := make(chan int, 5)
	for j := 1; j <= 5; j++ {
		burstyRequests <- j
	}
	close(burstyRequests)
	for breq := range burstyRequests {
		<-burstyLimiter
		fmt.Println("reqeust", breq, time.Now())
	}

}
