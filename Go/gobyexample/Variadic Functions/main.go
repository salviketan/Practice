package main

import "fmt"

func main() {
	sum(1, 2, 3, 1)

	num := []int{1, 2, 3, 4}
	sum(num...)
}

func sum(nums ...int) {
	fmt.Println(nums, " ")
	var total int
	for _, val := range nums {
		total += val
	}
	fmt.Println(total)
}
