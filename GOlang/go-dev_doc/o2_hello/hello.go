// // Tutorial 2: Call your code from another module

// package main

// import (
// 	"fmt"

// 	"example.com/greetings"
// )

// func main() {
// 	// Get a greeting message and print it.
// 	message := greetings.Hello("Gladys")
// 	fmt.Println(message)
// }

// // Tutorial 3: Return and handle an error
// package main

// import (
// 	"fmt"
// 	"log"

// 	"example.com/greetings"
// )

// func main() {
// 	// Set properties of the predefined Logger, including
// 	// the log entry prefix and a flag to disable printing
// 	// the time, source file, and line number.
// 	log.SetPrefix("greetings: ")
// 	log.SetFlags(0)

// 	// Request a greeting message.
// 	message, err := greetings.Hello("")
// 	// If an error was returned, print it to the console and
// 	// exit the program.
// 	if err != nil {
// 		log.Fatal(err)
// 	}

// 	// If no error was returned, print the returned message
// 	// to the console.
// 	fmt.Println(message)
// }

// // Tutorial 4: Return a random greeting
// package main

// import (
// 	"fmt"
// 	"log"

// 	"example.com/greetings"
// )

// func main() {
// 	// Set properties of the predefined Logger, including
// 	// the log entry prefix and a flag to disable printing
// 	// the time, source file, and line number.
// 	log.SetPrefix("greetings: ")
// 	log.SetFlags(0)

// 	// Request a greeting message.
// 	message, err := greetings.Hello("Chomu")
// 	// If an error was returned, print it to the console and
// 	// exit the program.
// 	if err != nil {
// 		log.Fatal(err)
// 	}

// 	// If no error was returned, print the returned message
// 	// to the console.
// 	fmt.Println(message)
// }

// Tutorial 5: Return greetings for multiple people
package main

import (
	"fmt"
	"log"

	"example.com/greetings"
)

func main() {
	// Set properties of the predefined Logger, including
	// the log entry prefix and a flag to disable printing
	// the time, source file, and line number.
	log.SetPrefix("greetings: ")
	log.SetFlags(0)

	// A slice of names.
	names := []string{"Gladys", "Samantha", "Darrin"}

	// Request greeting messages for the names.
	messages, err := greetings.Hellos(names)
	if err != nil {
		log.Fatal(err)
	}
	// If no error was returned, print the returned map of
	// messages to the console.
	fmt.Println(messages)
}
