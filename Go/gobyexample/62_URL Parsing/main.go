package main

import (
	"fmt"
	"net"
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
	p, _ := u.User.Password()
	fmt.Println(p)

	fmt.Println(u.Host)
	host, port, _ := net.SplitHostPort(u.Host)
	fmt.Println("derived from net.SplitHostPort(string) = Host:", host, "Port:", port)
	fmt.Println("derived from obj.Hostname(): ", u.Hostname())
	fmt.Println("derived from obj.Port(): ", u.Port())

	fmt.Println(u.Path)
	fmt.Println(u.Fragment)

	fmt.Println(u.RawQuery)
	m, _ := url.ParseQuery(u.RawQuery)
	fmt.Println("derived from obj.ParseQuery(string): ", m)
	fmt.Println("derived from obj.Query(): ",u.Query())
	fmt.Println(m["k"])
	fmt.Println(m["k"][0])
}