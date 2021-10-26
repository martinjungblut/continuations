package main

import "fmt"

func classicFib(a uint64, b uint64, counter uint64, limit uint64) uint64 {
	if counter > limit {
		return a
	} else if counter == limit {
		return b
	} else {
		return classicFib(b, a+b, counter+1, limit)
	}
}

func main() {
	fmt.Printf("%v\n", classicFib(0, 1, 1, 5_000_000))
}
