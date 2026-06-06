package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func main() {
	path := filepath.Join(os.TempDir(), "defer.txt")
	f := createFile(path)
	defer closeFile(f)
	write2File(f)
}

func createFile(p string) *os.File {
	f, err := os.Create(p)
	if err != nil {
		panic(err)
	}
	fmt.Println("created file")
	return f
}

func write2File(f *os.File) {
	fmt.Println("writing to file")
	fmt.Fprintln(f, "data")
}

func closeFile(f *os.File) {
	err := f.Close()
	if err != nil {
		panic(err)
	}
	fmt.Println("closed file")
}
