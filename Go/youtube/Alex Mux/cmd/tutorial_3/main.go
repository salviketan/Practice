package main

import (
	"errors"
	"fmt"
)

func main() {
	var printValue string = "Hello World!"
	printMe(printValue)

	var numerator = 0
	var denominator = 0
	// var result = intDivision(numerator, denominator)
	// fmt.Println(result)

	var result, remainder, err = intDivisionRemainder(numerator, denominator)
	// if statement structure
	if err != nil {
		fmt.Printf("%v\n", err.Error())
	} else if remainder == 0 {
		fmt.Printf("The result of the interger division is %v\n", result)
	} else {
		fmt.Printf("Division: %v, Remainder: %v\n", result, remainder)
	}
	// switch statement structure
	switch {
	case err != nil:
		fmt.Printf("%v\n", err.Error())
	case remainder == 0:
		fmt.Printf("The result of the interger division is %v\n", result)
	default:
		fmt.Printf("Division: %v, Remainder: %v\n", result, remainder)
	}
	// switch with condition statement structure
	switch remainder {
	case 0:
		fmt.Printf("The division was exact\n")
	case 1, 2:
		fmt.Printf("The division was close\n")
	default:
		fmt.Printf("The division was not close\n")
	}

}

func printMe(printValue string) {
	fmt.Println(printValue)
}

func intDivision(numerator int, denominator int) int {
	var result int = numerator / denominator
	return result
}

func intDivisionRemainder(numerator int, denominator int) (int, int, error) {
	var err error
	if denominator == 0 {
		err = errors.New("Can not divide by zero")
		return 0, 0, err
	}
	var division int = numerator / denominator
	var remainder int = numerator % denominator

	return division, remainder, err
}
