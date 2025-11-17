package main

import (
	"fmt"
	"time"
)

func main() {
	var i = 3

	fmt.Println("1. Basic switch")
	switch i {
	case 1:
		fmt.Println("one")
	case 2:
		fmt.Println("two")
	case 3:
		fmt.Println("three")
	}

	fmt.Println("\n2. We can use commas to separate multiple expressions in the same case statement.")
	switch time.Now().Weekday() {
	case time.Saturday, time.Sunday:
		fmt.Println("Weekends")
	default:
		fmt.Println("weekday")
	}

	fmt.Println("\n3. switch without an expression is an alternate way to express if/else logic")
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("Its before noon")
	default:
		fmt.Println("Its after noon")
	}

	fmt.Println("\n4. A 'type switch' compares types instead of values. You can use this to discover the type of an interface value.")
	whatAmI := func(i interface{}) {
		switch t := i.(type) {
		case bool:
			fmt.Println("I'am boolean")
		case int:
			fmt.Println("I'am int")
		default:
			fmt.Printf("Don't know type %T\n", t)
		}
	}

	whatAmI(true)
	whatAmI(1)
	whatAmI("hey")
}
