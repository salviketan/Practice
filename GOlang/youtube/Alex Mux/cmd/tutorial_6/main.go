package main

import (
	"fmt"
)

type gasEngine struct {
	mpg     uint8
	gallons uint8
	user    owner
	// owner    //1. we can do this too
}

type owner struct {
	name string
}

type electricEngine struct {
	mpkwh uint8
	kwh   uint8
}

func (e gasEngine) milesLeft() uint8 {
	return e.gallons * e.mpg
}

func (e electricEngine) milesLeft() uint8 {
	return e.kwh * e.mpkwh
}

type engine interface {
	milesLeft() uint8
}

func canMakeIt(e engine, miles uint8) {
	if miles <= e.milesLeft() {
		fmt.Println("You can make it")
	} else {
		fmt.Println("Can not make refill")
	}
}

func main() {
	var gasCar gasEngine = gasEngine{mpg: 25, gallons: 30, user: owner{name: "ketan"}}
	fmt.Println(gasCar)
	fmt.Println(gasCar.user)
	fmt.Println(gasCar.user.name)
	// var gasCar gasEngine = gasEngine{25, 30, owner{"ketan"}}    //can do this to
	// fmt.Println(gasCar.name)    //1. Then you can directly access owner struct var like this

	var electricCar electricEngine = electricEngine{25, 30}
	fmt.Println(electricCar)
	electricCar.mpkwh = 20
	fmt.Println(electricCar)

	// anonymous struct
	var myCar3 = struct {
		mpg     uint8
		gallons uint8
	}{25, 15}
	fmt.Println(myCar3.mpg, myCar3.gallons)

	var result = gasCar.milesLeft()
	fmt.Println(result)

	canMakeIt(gasCar, 200)
	canMakeIt(electricCar, 50)
}
