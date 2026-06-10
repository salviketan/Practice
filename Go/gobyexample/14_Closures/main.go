package main

import "fmt"

func intSeq() func() int {
	i := 0
	return func() int {
		i++
		return i
	}

}

func main() {

	nextInt := intSeq()

	fmt.Println("Closer 1: ",nextInt())
	fmt.Println("Closer 1: ",nextInt())
	fmt.Println("Closer 1: ",nextInt())

	nextInts := intSeq()
	fmt.Println("Closer 2: ",nextInts())
	fmt.Println("Closer 1: ",nextInt())
	fmt.Println("Closer 2: ",nextInts())

}
