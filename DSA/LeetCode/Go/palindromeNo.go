package main

import "fmt"

func isPalindrome(x int) bool {
	var reverse int
	if x < 0 || (x%10 == 0 && x != 0) {
		return false
	}
	for x > reverse {
		reverse = reverse*10 + (x % 10)
		x /= 10
	}

	return reverse == x || reverse/10 == x
}

func main() {
	fmt.Println(isPalindrome(121))
}
