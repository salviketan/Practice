package main

import "fmt"

func myPointer() {
	var p *int32 = new(int32)
	var i int32 = 7
	fmt.Printf("The value p points to is: %v\n", *p) // Value stored at this location (use *) :- called direferencing pointer
	fmt.Printf("The value of i is: %v , value inside p: %v\n", i, p)

	*p = 10 // It changes value stored inside memory location pointed by the pointer - changes value of 'i'
	fmt.Printf("The value p points to is: %v\n", *p)
	fmt.Printf("The value of i is: %v , value inside p: %v\n", i, p)

	p = &i // It stores memory address of variable 'i' in pointer var 'p'
	*p = 1
	fmt.Printf("The value p points to is: %v\n", *p)
	fmt.Printf("The value of i is: %v , value inside p: %v\n", i, p)

	var slice = []int32{1, 2, 3}
	var sliceCopy = slice
	sliceCopy[2] = 4
	fmt.Printf("slice: %v, sliceCopy: %v", slice, sliceCopy)

}

func main() {
	var thing1 = [5]float64{1, 2, 3, 4, 5}
	fmt.Printf("The memory location of thing1 array is: %p", &thing1)
	var result [5]float64 = square(thing1)
	fmt.Printf("\nThe result is: %v", result)
	fmt.Printf("\nThe value of thing1 is: %v", thing1)

	var light_result [5]float64 = light_square(&thing1)
	fmt.Printf("\nThe result is: %v", light_result)
	fmt.Printf("\nThe value of thing1 is: %v", thing1)

}

func square(thing2 [5]float64) [5]float64 {
	fmt.Printf("\nThe memory location of thing2 array is: %p", &thing2)
	for i := range thing2 {
		thing2[i] = thing2[i] * thing2[i]
	}
	return thing2
}

func light_square(thing3 *[5]float64) [5]float64 {
	fmt.Printf("\nThe memory location of thing3 array is: %p", thing3)
	for i := range thing3 {
		thing3[i] = thing3[i] * thing3[i]
	}
	return *thing3
}
