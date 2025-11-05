package main

import "fmt"

func main() {
	// var intArr [3]int32

	// var intArr [3]int32 = [3]int32{1, 2, 3}

	// intArr := [3]int32{1, 2, 3}

	intArr := [...]int32{1, 2, 3}

	fmt.Println(intArr)
	fmt.Println(intArr[0])
	fmt.Println(intArr[1:3])

	fmt.Println(&intArr[0])
	fmt.Println(&intArr[1])
	fmt.Println(&intArr[2])

	var intSlice []int32 = []int32{4, 5, 6}
	fmt.Println(intSlice)
	fmt.Printf("The lenght is %v and capacity is %v\n", len(intSlice), cap(intSlice))
	intSlice = append(intSlice, 7)
	fmt.Printf("The lenght is %v and capacity is %v\n", len(intSlice), cap(intSlice))
	fmt.Println(intSlice)
	// fmt.Println(intSlice[4])

	var intSlice2 []int32 = []int32{8, 9}

	intSlice = append(intSlice, intSlice2...)
	fmt.Println(intSlice)

	intSlice3 := make([]int32, 3, 8)
	fmt.Println(intSlice3)
	fmt.Printf("The lenght is %v and capacity is %v\n", len(intSlice3), cap(intSlice3))

	var myMap map[string]uint8 = make(map[string]uint8)
	fmt.Println(myMap)

	var myMap2 = map[string]uint8{"Adam": 28, "Jacob": 29}
	myMap2["Jason"] = 35
	fmt.Println(myMap2)
	fmt.Println(myMap2["Adam"])
	fmt.Println(myMap2["James"])

	var age, ok = myMap2["James"]
	if ok {
		fmt.Printf("The age is %v", age)
	} else {
		fmt.Print("Invalid Name\n")
	}

	for name := range myMap2 {
		fmt.Printf("Name: %v\n", name)
	}

	for name, age := range myMap2 {
		fmt.Printf("Name: %v, age: %v\n", name, age)
	}

	for idx, val := range intArr {
		fmt.Printf("Index: %v, Value: %v \n", idx, val)
	}

	var i int = 0
	for i < 5 {
		fmt.Println(i)
		i = i + 1
	}

	for {
		if i >= 10 {
			break
		}
		fmt.Println(i)
		i = i + 1
	}

	for i = 6; i < 10; i++ {
		fmt.Println(i)
	}

}
