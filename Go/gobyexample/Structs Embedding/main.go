package main

import "fmt"

type base struct {
	num int
}

func (b base) discribe() string {
	return fmt.Sprintf("base with num=%v", b.num)
}

type container struct {
	base
	str string
}

func main() {
	co := container{
		base: base{
			num: 1,
		},
		str: "some name",
	}

	fmt.Printf("co={num: %d, str: %s}\n", co.num, co.str)
	fmt.Printf("also num: %v\n", co.base.num)

	fmt.Println("discribe:", co.discribe())

	type discriber interface {
		discribe() string
	}

	var d discriber = co
	fmt.Printf("describer: %s", d.discribe())
}
