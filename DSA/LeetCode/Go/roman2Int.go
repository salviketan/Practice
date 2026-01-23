package main

import "fmt"

func romanToInt_1(s string) int {
	value := map[rune]int{
		'I': 1, 'V': 5, 'X': 10, 'L': 50,
		'C': 100, 'D': 500, 'M': 1000,
	}

	total := 0
	i := 0
	for i < len(s) {
		if (i+1) < len(s) && value[rune(s[i])] < value[rune(s[i+1])] {
			total += value[rune(s[i+1])] - value[rune(s[i])]
			i += 2
		} else {
			total += value[rune(s[i])]
			i += 1
		}
	}

	return total
}

// Approach 2: Left-to-Right Pass Improvalueed
func romanToInt_2(s string) int {
	value := map[string]int{
		"I": 1, "V": 5, "X": 10, "L": 50,
		"C": 100, "D": 500, "M": 1000, "IV": 4,
		"IX": 9, "XL": 40, "XC": 90, "CD": 400,
		"CM": 900,
	}

	total := 0
	i := 0
	for i < len(s) {
		if i < (len(s)-1) && value[string(s[i])] < value[string(s[i+1])] {
			total += value[string(s[i:i+2])]
			i += 2
		} else {
			total += value[string(s[i])]
			i += 1
		}
	}

	return total
}

// Approach 3: Right-to-Left pass
func romanToInt_3(s string) any {
	return nil
}

func main() {
	inp_str := "MCMXCIV"

	fmt.Println("romanToInt_1: ", romanToInt_1(inp_str))
	fmt.Println("romanToInt_2: ", romanToInt_2(inp_str))
	fmt.Println("romanToInt_3: ", romanToInt_3(inp_str))
}
