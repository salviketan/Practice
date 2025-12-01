package main

import (
	"fmt"
	"iter"
	"slices"
)

type List[T any] struct {
	head, tail *element[T]
}

type element[T any] struct {
	next *element[T]
	val  T
}

func (lst *List[T]) Push(v T) {
	if lst.tail == nil {
		lst.head = &element[T]{val: v}
		lst.tail = lst.head
	} else {
		lst.tail.next = &element[T]{val: v}
		lst.tail = lst.tail.next
	}
}

func (lst *List[T]) iterAll() iter.Seq[T] {
	return func(yeild func(T) bool) {
		for e := lst.head; e != nil; e = e.next {
			if !yeild(e.val) {
				return
			}
		}
	}
}

func genFib() iter.Seq[int] {
	return func(yeild func(int) bool) {
		a, b := 1, 1
		for {
			if !yeild(a) {
				return
			}
			a, b = b, a+b
		}
	}
}

func main() {
	lst := List[int]{}
	lst.Push(10)
	lst.Push(13)
	lst.Push(23)

	fmt.Println("lst obj: ", lst, &lst.head, &lst.tail, &lst.tail.next)

	fmt.Println("iter obj: ", lst.iterAll())

	// Iterate using for loop and range
	for e := range lst.iterAll() {
		fmt.Println(e)
	}

	// Iterate using slices.Collect() method. Use slices package.
	all := slices.Collect(lst.iterAll())
	fmt.Println("all: ", all)

	// Iterate using iter.Pull() and next() method. We call next() to get next sequence in iterator.
	all2 := lst.iterAll()
	next, stop := iter.Pull(all2)
	defer stop()
	fmt.Println(next())
	fmt.Println(next())

	for n := range genFib() {
		if n >= 10 {
			break
		}
		fmt.Println(n)
	}

}
