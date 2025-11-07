package main

import (
	"fmt"
)

type gasEngine struct {
	mpg     uint8
	gallons uint8
	user    owner
	// owner    //we can do this too
}

type owner struct {
	name string
}

func main() {
	var myCar gasEngine = gasEngine{mpg: 25, gallons: 30, user: owner{name: "ketan"}}
	fmt.Println(myCar)
	fmt.Println(myCar.user.name)

	var myCar2 gasEngine = gasEngine{25, 30, owner{"ketan"}}
	fmt.Println(myCar2)
	myCar2.mpg = 20
	fmt.Println(myCar2)
	fmt.Println(myCar.user)

}
