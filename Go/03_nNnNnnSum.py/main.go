package main

import (
	"fmt"
)

func main()  {
	var input int 
	fmt.Println("Enter digit (0-9):")
	fmt.Scan(&input)

	n := input
	nn := 10*n+n
	nnn := 10*nn+n
	result := n + nn + nnn
	fmt.Println("1 result: ",result)

	// Loop approach
	result = 0
	var i int = 0
	var value int
	for i < 3 {
		value = 10 * value + input
		result += value
		i++
	}
	fmt.Println("2 result: ",result)
}
