package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {
	norm_string := "ketan"
	unique_string := "kèťãŉ"

	fmt.Println("len n:", len(norm_string))
	fmt.Println("len u:", len(unique_string))

	fmt.Println("rune count n:", utf8.RuneCountInString(norm_string))
	fmt.Println("rune count u:", utf8.RuneCountInString(norm_string))

	fmt.Printf("\n---findChar---\n")
	findChar(unique_string, '-')
	findChar(unique_string, 'ã')
	findChar(unique_string, 'ŉ')

	fmt.Printf("\n---findChar1---\n")
	findChar1(unique_string, '-')
	findChar1(unique_string, 'ã')
	findChar1(unique_string, 'ŉ')

}

func findChar(s string, c rune) bool {
	for idx, runeValue := range s {
		if runeValue == c {
			fmt.Println(idx, runeValue, c)
			return true
		}
	}
	fmt.Println("Char not in string")
	return false
}

func findChar1(s string, c rune) bool {
	for i, v := range s {
		switch v {
		case c:
			fmt.Println("found a at: ", i, v)
			return true
		case c:
			fmt.Println("found e at: ", i, v)
			return true
		case c:
			fmt.Println("found t at: ", i, v)
			return true
		case c:
			fmt.Println("found n at: ", i, v)
			return true
		default:
			fmt.Println("No match", i)
		}
	}
	fmt.Println("Char not in string")
	return false
}
