package main

import (
	"fmt"
	"time"
)

func main() {
	jobs := make(chan int, 5)
	done := make(chan bool)

	go func() {
		for {
			j, more := <-jobs
			if more {
				fmt.Println("Recieved job: ", j)
			} else {
				fmt.Println("Recieved all jobs")
				done <- true
				return
			}
		}
	}()

	for i := 1; i <= 3; i++ {
		jobs <- i
		fmt.Println("Sent job: ", i)
		time.Sleep(1 * time.Millisecond) //This line changes output execution
	}
	close(jobs)
	fmt.Println("Sent all jobs")

	<-done

	_, ok := <-jobs
	fmt.Println("Recieved more job: ", ok)
}
