package main

import (
	"fmt"
	"sync"
	"time"
)

// var m = sync.Mutex{}
var wg = sync.WaitGroup{}
var dbData = []string{"id1", "id2", "id3", "id4", "id5"}

var result = []string{}

func main() {
	t0 := time.Now()
	for i := 0; i < len(dbData); i++ {
		wg.Add(1)
		go dbCall(i)
	}
	wg.Wait()
	fmt.Printf("\nTotal execution time: %v", time.Since(t0))
	fmt.Println(result)
}

func dbCall(i int) {
	var delay float32 = 2000
	time.Sleep(time.Duration(delay) * time.Millisecond)
	// m.Lock()
	fmt.Println("The result from the database is: ", dbData[i])
	result = append(result, dbData[i])
	// m.Unlock()
	wg.Done()
}
