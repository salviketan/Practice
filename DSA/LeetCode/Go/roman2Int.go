package main

import "fmt"

func romanToInt(s string, v map[string]int) int {
	total := 0
	i := 0
	for i < len(s) {
		if (i+1) < len(s) && v[string(s[i])] < v[string(s[i+1])] {
			total += v[string(s[i+1])] - v[string(s[i])]
			i += 2
		} else {
			total += v[string(s[i])]
			i += 1
		}
	}

	return total
}

func main() {
	inp_str := "MCMXCIV"
	val := map[string]int{
		"I": 1, "V": 5, "X": 10, "L": 50,
		"C": 100, "D": 500, "M": 1000,
	}

	fmt.Println("romanToInt: ", romanToInt(inp_str, val))

}
