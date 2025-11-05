package main

import (
	"fmt"
	"unicode/utf8"
)

func foo() string {
	ret := "This is foo function."
	return ret
}

func main() {
	var intNum int = 32767
	fmt.Println(intNum)

	var floatNum float64 = 12345678.9
	fmt.Println(floatNum)

	var floatNum32 float32 = 10.1
	var intNum32 int32 = 2
	var result float32 = floatNum32 + float32(intNum32)
	fmt.Println(result)

	var intNum1 int = 3
	var intNum2 int = 2
	fmt.Println(intNum1 / intNum2)
	fmt.Println(intNum1 % intNum2)

	var myString string = "Hello" + " " + "World"
	fmt.Println(myString)

	fmt.Println(len("&"))
	fmt.Println(utf8.RuneCountInString("&"))

	var myRune rune = 'a'
	fmt.Println(myRune)

	var myBoolean bool = false
	fmt.Println(myBoolean)

	var intNum3 int
	fmt.Println(intNum3)

	var myVarT = "text1"
	fmt.Println(myVarT)

	myVar1 := "text2"
	fmt.Println(myVar1)

	var1, var2 := 1, 2
	fmt.Println(var1, var2)

	var myVar2 string = foo()
	fmt.Println(myVar2)

	const myConst string = "const value"
	fmt.Println(myConst)

	const pi float32 = 3.1415
	fmt.Println(pi)

}
