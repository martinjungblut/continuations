package main

import "fmt"

func whatever(args ...interface{}) {
	fmt.Printf("Length: %v\n", len(args))

	for _, arg := range args {
		fmt.Printf("%v\n", arg)
	}
}

func main() {
	whatever(1, 2, 3)
}
