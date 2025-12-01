package main

import (
	"errors"
)

func f(arg int) (int, error) {
	if arg == 2 {
		return -1, errors.New("can't work with 42")
	}
	return arg + 3, nil
}
