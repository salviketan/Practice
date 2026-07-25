package main

import (
	"fmt"
	"net/url"
)

func main()  {
	s, err := url.Parse("postgres://user:pass@host.com:5432/path?k=v#f")
	if err != nil{
		panic(err)
	}
	fmt.Println(s)
}