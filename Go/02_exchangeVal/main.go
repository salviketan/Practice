package main

import "fmt"


func main()  {
	// Inbuild go way just like python
	var a int8 = 1
	var b int8 = 2

	a, b = b ,a
	fmt.Println("a:",a,"b:",b)

	// The Mathematical Way (Addition/Subtraction)
	a, b = 1, 2
	a = a + b
	b = a - b
	a = a - b
	fmt.Println("a:",a,"b:",b)

	// The "Digital" Way (XOR)
	a, b = 1, 2
	a = a ^ b
	fmt.Println("EOR 1s:- a:",a,"b:",b)
	b = a ^ b
	fmt.Println("EOR 2s:- a:",a,"b:",b)
	a = a ^ b
	fmt.Println("EOR 3s:- a:",a,"b:",b)

}