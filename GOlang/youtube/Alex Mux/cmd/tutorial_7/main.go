package main

import "fmt"

func main() {
	var p *int32 = new(int32)
	var i int32 = 7

	fmt.Printf("The value p points to is: %v\n", *p)
	fmt.Printf("The value of i is: %v , value inside p: %v\n", i, p)

	p = &i
	fmt.Printf("The value p points to is: %v\n", *p)
	fmt.Printf("The value of i is: %v , value inside p: %v\n", i, p)

	*p = 10
	fmt.Printf("The value p points to is: %v\n", *p)
	fmt.Printf("The value of i is: %v , value inside p: %v\n", i, p)

	var slice = []int32{1, 2, 3}
	var sliceCopy = slice
	sliceCopy[2] = 4
	fmt.Printf("slice: %v, sliceCopy: %v", slice, sliceCopy)

}
