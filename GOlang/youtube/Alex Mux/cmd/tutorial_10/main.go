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
}

func sumSlice[T int | float32 | float64](slice []T) T {
	var sum T
	for _, v := range slice {
		sum += v
	}
	return sum
}
