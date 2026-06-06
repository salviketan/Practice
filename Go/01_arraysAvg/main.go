package main

import (
	"fmt"
	"strconv"
	"strings"
)

func Average(l *[]int) float64 {
	var total int
	for _, v := range *l {
		total += v
	}
	return  float64(total)/float64(len(*l))
}


func Str2ints(strs *[]string) []int {
	ints := make([]int, 0, len(*strs))

	for _, s := range *strs{
		s := strings.TrimSpace(s)
		if s == "" || s == " " {continue}
		v, err := strconv.Atoi(s)
		if err != nil { fmt.Println("error: ", err)}
		ints = append(ints, v)
	}

	return ints
}

func main()  {
	var input string
	fmt.Println("Enter comma-separated values:")
	fmt.Scan(&input)

	strs := strings.Split(input, ",")

	values := Str2ints(&strs)

	result := Average(&values)
	fmt.Printf("result: %.2f\n", result)
}