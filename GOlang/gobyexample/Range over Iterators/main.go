package main

type List[T any] struct {
	head, tail *element[T]
}

type element[T any] struct {
	next *element[T]
	val  T
}

func (lst *List[T]) AllElements() []T {
	var elem []T

	for e := lst.head; e != nil; e = e.next {
		elem = append(elem, e.val)
	}
	return elem
}
