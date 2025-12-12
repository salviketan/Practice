package main

import (
	"fmt"
	"math"
)

type rect struct {
	height, width float64
}

type circle struct {
	radius float64
}

type geometry interface {
	area() float64
	premis() float64
}

func (r rect) area() float64 {
	return r.height * r.width
}

func (r rect) premis() float64 {
	return 2*r.height + 2*r.width
}

func (c circle) area() float64 {
	return math.Pi * c.radius * c.radius
}

func (c circle) premis() float64 {
	return 2 * math.Pi * c.radius
}

func measure(g geometry) {
	fmt.Println(g)
	fmt.Println(g.area())
	fmt.Println(g.premis())
}

func detectCircle(g geometry) {
	if c, ok := g.(circle); ok {
		fmt.Println("Circle with radius", c.radius)
	}
}

func main() {
	r := rect{height: 4, width: 3}
	c := circle{radius: 5}

	measure(r)
	measure(c)

	detectCircle(r)
	detectCircle(c)
}
