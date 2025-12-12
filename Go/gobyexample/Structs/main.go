package main

import (
	"fmt"
)

func main() {
	fmt.Println(person{"Bob", 23})

	fmt.Println(person{name: "Alice", age: 20})

	fmt.Println(person{name: "Fred"})

	fmt.Println(&person{name: "Ann", age: 26})

	fmt.Println(newPerson("Jon"))

	s := person{name: "Sean", age: 50}

	fmt.Println(s.name)

	sp := &s
	fmt.Println(sp.age)

	sp.age = 52
	fmt.Println(sp)
	fmt.Println(s)

	dog := struct {
		name   string
		isGood bool
	}{
		"Rob",
		true,
	}
	fmt.Println(dog)

}

type person struct {
	name string
	age  int
}

func newPerson(n string) *person {
	p := person{name: n}
	p.age = 42

	return &p
}
