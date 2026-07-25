package main

import (
	"fmt"
	"net/url"
)

func main()  {
	l, err := url.Parse("postgres://user:pass@host.com:5432/path?k=v#f")
	if err != nil{
		panic(err)
	}
	fmt.Println(l)

	s := "postgres://user:pass@host.com:5432/path?k=v#f"

	u, err := url.Parse(s)
	if err != nil{
		panic(err)
	}
	fmt.Println("Scheme:",u.Scheme)

    fmt.Println("User:",u.User)
    fmt.Println(u.User.Username())

}