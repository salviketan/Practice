package main

import "fmt"

type rect struct {
	width, height int
}

func (r *rect) area() int {
	return r.width * r.height
}

func (r rect) premis() int {
	return 2*r.width + 2*r.height
}

func main() {
	r := rect{5, 6}
	fmt.Println(r.area())
	fmt.Println(r.premis())

	rp := &r
	fmt.Println(r.area())
	fmt.Println(r.premis())

	fmt.Println(r, &r)
	fmt.Printf("%p\n", &r)
	fmt.Println(rp, *rp, &rp)
	fmt.Printf("%p, %p\n", rp, &rp)

}
