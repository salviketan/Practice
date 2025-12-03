package main

import (
	"errors"
	"fmt"
)

func f(arg int) (int, error) {
	if arg == 42 {
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
	is_error := makeTea(arg)
	if is_error != nil {
		fmt.Println("error:", is_error)
	} else {
		fmt.Println("arg: ", arg)
	}

	for _, i := range []int{7, 42} {
		if r, e := f(i); e != nil {
			fmt.Println("f failed:", e)
		} else {
			fmt.Println("f worked:", r)
		}
	}

	for i := range 5 {
		if e := makeTea(i); e != nil {
			// switch e {
			// case ErrOutOfTea:
			// 	fmt.Println("We should buy new tea!")
			// case ErrPower:
			// 	fmt.Println("Now it is dark.")
			// default:
			// 	fmt.Printf("unknown error %s\n", e)
			// }
			// Or
			if errors.Is(e, ErrOutOfTea) {
				fmt.Println("We should buy new tea!")
			} else if errors.Is(e, ErrPower) {
				fmt.Println("Now it is dark.")
			} else {
				fmt.Printf("unknown error %s\n", e)
			}

			continue
		}
		fmt.Println("Tea is ready!")
	}
}
