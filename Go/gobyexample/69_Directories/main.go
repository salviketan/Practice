package main

import (
	"fmt"
	"io/fs"
	"os"
	"path/filepath"
)

func check(e error)  {
	if e != nil {
		panic(e)
	}
}

func main()  {
	err := os.Mkdir("subdir", 0755)
	check(err)

	defer os.RemoveAll("subdir")

	createEmptyfile := func (name string)  {
		d := []byte("")
		check(os.WriteFile(name, d, 0644))
	}

	createEmptyfile("subdir/file1")

	err = os.MkdirAll("subdir/parent/child", 0755)
	check(err)

	createEmptyfile("subdir/parent/file2")
	createEmptyfile("subdir/parent/file3")
	createEmptyfile("subdir/parent/child/file4")

	c, err := os.ReadDir("subdir/parent")
	check(err)

	fmt.Println("Listing subdir/parent")
	for _, entry := range c {
		fmt.Println(" ", entry.Name(), entry.IsDir())
	}

	err = os.Chdir("subdir/parent/child")
	check(err)

	c, err = os.ReadDir(".")
	check(err)

	fmt.Println("Listing subdir/parent/child")
	for _, entry := range c {
		fmt.Println(" ", entry.Name(), entry.IsDir())
	}

	err = os.Chdir("../../..")
	check(err)

	fmt.Println("Visiting subdir")
	err = filepath.WalkDir("subdir", visit)
	check(err)
}

func visit(path string, d fs.DirEntry, err error)  error {
	if err != nil {
		return err
	}
	fmt.Println(" ", path, d.IsDir())
	return nil
}