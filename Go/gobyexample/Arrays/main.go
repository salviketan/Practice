package main

import (
	"fmt"
)

func main() {
	var a [5]int
	fmt.Println("emp: ", a)

	a[4] = 100
	fmt.Println("set: ", a)
	fmt.Println("get: ", a[4])
	fmt.Println("len: ", len(a))

	var b [5]int = [5]int{1, 2, 3, 4, 5}
	fmt.Println("dcl: ", b)

	var c = [...]int{1, 2, 3, 4, 5}
	fmt.Println("dcl: ", c)

	d := [5]int{100, 3: 400, 500}
	fmt.Println("idx: ", d)

	var twoD [2][3]int
	for i := range 2 {
		for j := range 3 {
			twoD[i][j] = i + j
		}
	}
	fmt.Println("2D: ", twoD)

	twoD = [2][3]int{
		{1, 2, 3},
		{1, 2, 3},
	}
	fmt.Println("2D: ", twoD)
}
