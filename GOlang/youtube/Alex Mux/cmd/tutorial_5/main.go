package main

import (
	"fmt"
)

func main() {
	var myString string = "résumé"
	fmt.Println(myString)
	var idx = myString[3]
	fmt.Printf("%v, %T\n", idx, idx)

	for idx, val := range myString {
		fmt.Println(idx, val)
	}
}
