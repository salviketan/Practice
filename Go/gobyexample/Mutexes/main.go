package main

import (
	"fmt"
	"runtime"
	"sync"
)

type Container struct {
	mu       sync.Mutex
	counters map[string]int
}

func (c *Container) inc(name string) {

	c.mu.Lock()
	defer c.mu.Unlock()
	c.counters[name]++
}

func main() {
	fmt.Println("Goroutines at start:", runtime.NumGoroutine())

	c := Container{
		counters: map[string]int{"a": 0, "b": 0},
	}

	var wg sync.WaitGroup

	doIncrement := func(name string, n int) {
		for range n {
			c.inc(name)
		}
	}

	wg.Go(func() { doIncrement("a", 10000) })

	wg.Go(func() { doIncrement("a", 10000) })

	wg.Go(func() { doIncrement("b", 10000) })

	wg.Wait()

	fmt.Println("counters:", c.counters)

	fmt.Println("Goroutines at end:", runtime.NumGoroutine())

}
