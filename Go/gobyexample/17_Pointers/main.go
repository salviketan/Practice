package main

import "fmt"

func zeroVal(ival int) {
	ival = 1
	fmt.Printf("Creates new obj ival:- %v, %p\n", ival, &ival)
}

func zeroPtr(iptr *int) {
	*iptr = 1
	fmt.Printf("Refers same obj iptr:- %v, %v, %p\n", iptr, *iptr, &iptr)
}

func main() {
	i := 0
	fmt.Println(i)

	zeroVal(i)
	fmt.Println(i)

	zeroPtr(&i)
	fmt.Println(i)

	fmt.Printf("Original obj:- %v, %v\n", i, &i)

}
