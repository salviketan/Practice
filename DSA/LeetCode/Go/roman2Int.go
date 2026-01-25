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
// My approach
func romanToInt_3(s string) int {
	values := map[rune]int{
		'I': 1, 'V': 5, 'X': 10, 'L': 50,
		'C': 100, 'D': 500, 'M': 1000,
	}

	total := 0
	i := len(s) - 1

	for i >= 0 {
		if i > 0 && values[rune(s[i-1])] < values[rune(s[i])] {
			total += values[rune(s[i])] - values[rune(s[i-1])]
			i -= 2
		} else {
			total += values[rune(s[i])]
			i -= 1
		}
	}

	return total
}

// LeetCode approach
func romanToInt_4(s string) int {

	values := map[rune]int{
		'I': 1, 'V': 5, 'X': 10, 'L': 50,
		'C': 100, 'D': 500, 'M': 1000,
	}

	lastValue := values[rune(s[len(s)-1])]
	total := lastValue

	for i := len(s) - 2; i >= 0; i-- {
		CurrentValue := values[rune(s[i])]

		if lastValue > CurrentValue {
			total -= CurrentValue
		} else {
			total += CurrentValue
		}
		lastValue = CurrentValue
	}

	return total
}

func main() {
	inp_str := "MCMXCIV"

	fmt.Println("romanToInt_1: ", romanToInt_1(inp_str))
	fmt.Println("romanToInt_2: ", romanToInt_2(inp_str))
	fmt.Println("romanToInt_3: ", romanToInt_3(inp_str))
	fmt.Println("romanToInt_4: ", romanToInt_4(inp_str))
}
