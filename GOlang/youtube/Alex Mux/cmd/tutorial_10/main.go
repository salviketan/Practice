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

	fmt.Println(isEmpty(intSlice))

	var gasCar = car[gasEngine]{
		make:   "Jeep",
		model:  "Rubicon",
		engine: gasEngine{kmph: 5, gallon: 10},
	}
	fmt.Println(gasCar)

	var electricCar = car[electricEngine]{
		make:   "Tesla",
		model:  "Model 3",
		engine: electricEngine{kwph: 6, mpkwh: 12},
	}
	fmt.Println(electricCar)
}

func sumSlice[T int | float32 | float64](slice []T) T {
	var sum T
	for _, v := range slice {
		sum += v
	}
	return sum
}

func isEmpty[T any](s []T) bool {
	return len(s) == 0
}

type gasEngine struct {
	kmph   float32
	gallon float32
}

type electricEngine struct {
	kwph  float32
	mpkwh float32
}

type car[T gasEngine | electricEngine] struct {
	make   string
	model  string
	engine T
}
