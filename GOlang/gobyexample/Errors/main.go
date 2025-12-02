package main

import (
	"errors"
	"fmt"
)

func f(arg int) (int, error) {
	if arg == 2 {
		return -1, errors.New("can't work with 42")
	}
	return arg + 3, nil
}

var ErrOutOfTea = errors.New("No more tea available")
var ErrPower = errors.New("Can't boil water")

func makeTea(arg int) error {
	switch arg {
	case 2:
		return ErrOutOfTea
	case 4:
		return ErrPower
	default:
		return nil
	}
	// Or
	// if arg == 2 {
	// 	return ErrOutOfTea
	// } else if arg == 4 {
	// 	return ErrPower
	// }

	// return nil
}

func main() {
	arg := 2

	result := makeTea(arg)

	if result != nil {
		fmt.Println("error:", result)
	} else {
		fmt.Println("arg: ", arg)
	}
}
