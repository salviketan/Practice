package main

import (
	"os"
	"path/filepath"
)

func main() {
	panic("A problem") //If you’d like to see the program try to create a temp file, comment this line

	path := filepath.Join(os.TempDir(), "file")	//file is created in "/tmp/" dir for safety and platform dependency
	_, err := os.Create(path)
	if err != nil {
		panic(err)
	}
}
