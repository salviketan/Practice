package main

import (
	"fmt"
	"io"
	"os"
	"path/filepath"
)



func check(e error)  {
	if e != nil {
		panic(e)
	}
}

func main()  {
	path := filepath.Join(os.TempDir(), "dat")
	dat, err := os.ReadFile(path)
	check(err)
	fmt.Print(string(dat))

	f, err := os.Open(path)
	check(err)

	b1 := make([]byte, 5)
	n1, err := f.Read(b1)
	check(err)
	fmt.Printf("%d bytes: %s\n", n1, string(b1[:n1]))

	o2, err := f.Seek(6, io.SeekStart)
	check(err)
	b2 := make([]byte, 2)
	n2, err:= f.Read(b2)
	check(err)
	fmt.Printf("%d bytes @ %d: ", n2, o2)
	fmt.Printf("%v\n",string(b2[:n2]))
}