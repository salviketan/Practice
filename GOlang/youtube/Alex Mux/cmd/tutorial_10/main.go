package main

import (
	"fmt"
)

func main() {
	var intSlice []int = []int{1, 2, 3, 4}
	var float32Slice []float32 = []float32{1, 2, 3, 4, 5}
	var float64Slice []float64 = []float64{1, 2, 3, 4, 5, 6}
	fmt.Println(sumSlice(intSlice))
	fmt.Println(sumSlice(float32Slice))
	fmt.Println(sumSlice(float64Slice))

	fmt.Println(sumSlice2(intSlice))

	var a petrolEngine = petrolEngine{kmph: 5, gallon: 2}

	fmt.Printf("%v", a.gallon)

	engine[petrolEngine](a)

}

func sumSlice[T int | float32 | float64](slice []T) T {
	var sum T
	for _, v := range slice {
		sum += v
	}
	return sum
}

func isEmpty[T any](slice []T) bool {
	retrun len(slice) == 0
}

type petrolEngine struct {
	kmph   int16
	gallon int16
}

type diselEngine struct {
	kmph   int16
	gallon int16
}

func engine[e petrolEngine | diselEngine](a e) {
	fmt.Println(a)
}
