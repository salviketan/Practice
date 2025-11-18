package main

import (
	"fmt"
	"slices"
)

func main() {
	var s []string
	fmt.Println("uninit:", s, s == nil, len(s), len(s) == 0)

	s = make([]string, 3, 5)
	fmt.Println("emp:", s, len(s), cap(s))

	s[0] = "a"
	s[1] = "b"
	s[2] = "c"
	fmt.Println("set:", s)
	fmt.Println("get:", s[1])

	s = append(s, "d")
	s = append(s, "e", "f")
	fmt.Println("apd:", s)

	var c = make([]string, len(s))
	copy(c, s)
	fmt.Println("exact cpy:", c)

	d := make([]string, 4)
	copy(d, s)
	fmt.Println("cpy-less cap:", d)

	var s1 []string = s[2:5]
	fmt.Println("s1:", s1)

	var s2 = s[:5]
	fmt.Println("s2:", s2)

	s3 := s[2:]
	fmt.Println("s3:", s3)

	s3 = []string{"g", "h", "i"}
	fmt.Println("dcl:", s3)

	s4 := []string{"g", "h", "i"}
	if slices.Equal(s3, s4) {
		fmt.Println("s3 == s4")
	}

	var twoD = make([][]int, 3)
	for i := range 3 {
		var innerLen = i + 1
		twoD[i] = make([]int, innerLen)
		for j := range innerLen {
			twoD[i][j] = i + j
		}
	}
	fmt.Println("2D:", twoD)

}
