package main

import (
	"fmt"
)

func main() {
	var i int = 0

	fmt.Println("1. For loop with a single condition - While loop with condition.")
	for i < 3 {
		fmt.Printf("i = %v\n", i)
		i++
	}

	fmt.Println("2. A classic initial/condition/after for loop.")
	for i := i; i < 6; i++ {
		fmt.Printf("i = %v\n", i)
	}

	fmt.Println("3. Basic iteration using range.")
	for i := range 3 {
		fmt.Printf("i = %v\n", i)
	}

	fmt.Println("4. Use 'break' to stop the loop - While loop without condition.")
	for {
		if i == 6 {
			break
		}
		fmt.Printf("i = %v\n", i)
		i++
	}

	fmt.Println("5.Skip iteration - continue to the next iteration of the loop.")
	for i := range 6 {
		if i == 3 {
			continue
		}
		fmt.Printf("i = %v\n", i)
		i++
	}

}
