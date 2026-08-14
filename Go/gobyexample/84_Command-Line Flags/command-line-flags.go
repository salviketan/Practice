package main

import (
	"flag"
	"fmt"
)


func main()  {
	wordPtr := flag.String("word", "foo", "a string")

	intPtr := flag.Int("numb", 7, "a int")
	boolPtr := flag.Bool("fork", false, "a bool")

	var svar string
	flag.StringVar(&svar, "svar", "bar", "a string var")

	flag.Parse()

	fmt.Println("word: ", * wordPtr)
	fmt.Println("numb: ", *intPtr)
	fmt.Println("fork: ", *boolPtr)
	fmt.Println("svar: ", svar)
	fmt.Println("tail: ", flag.Args())
}