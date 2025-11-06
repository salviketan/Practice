package main

import (
	"fmt"
)

func main() {
	var myString string = "résumé"
	fmt.Println(myString)
	var idx = myString[1]
	fmt.Printf("%v, %T\n", idx, idx)
	for idx, val := range myString {
		fmt.Println(idx, val)
	}
	fmt.Printf("The length of 'myString' is %v\n", len(myString))

	var myRune = []rune("résumé")
	fmt.Println(myRune)
	var index = myRune[1]
	fmt.Printf("%v, %T\n", index, index)
	for index, val := range myRune {
		fmt.Println(index, val)
	}

	fmt.Printf("The length of 'myRune' is %v\n", len(myRune))

	var myRune2 = 'a'
	fmt.Printf("myRune2 = %v", myRune2)

}
