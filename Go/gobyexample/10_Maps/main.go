package main

import (
	"fmt"
	"maps"
)

func main() {
	var m = make(map[string]int)
	fmt.Println("init:", m)

	m["k1"] = 1
	m["k2"] = 3
	fmt.Println("map:", m)

	fmt.Println("get:", m["k1"])

	fmt.Println("v3:", m["k3"])

	fmt.Println("len:", len(m))

	delete(m, "k2")
	fmt.Println("del-map:", m)

	clear(m)
	fmt.Println("clr-map:", m)

	_, prs := m["k2"]
	fmt.Println("prs:", prs)

	n := map[string]int{"foo": 1, "bar": 2}
	fmt.Println("map:", n)

	n1 := make(map[string]int)
	n1 = map[string]int{"foo": 1, "bar": 2}
	if maps.Equal(n, n1) {
		fmt.Println("n == n1")
	}
}
