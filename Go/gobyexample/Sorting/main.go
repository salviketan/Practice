package main

import (
	"fmt"
	"slices"
)

func main() {
	strs := []string{"b", "a", "c"}
	slices.Sort(strs)
	fmt.Println("Strings:", strs)

	ints := []uint8{7, 5, 2}
	slices.Sort(ints)
	fmt.Println("Ints:   ", ints)

	isSort := slices.IsSorted(ints)
	fmt.Println("Sorted:", isSort)
}
