package main

import "fmt"

type capture[T any] struct {
	continuation func(T)
}

func (c capture[T]) recall(input T) {
	if c.continuation != nil {
		c.continuation(input)
	}
}

func withcc[T any](c *capture[T], continuation func(T)) func(T) {
	c.continuation = continuation
	return continuation
}

func main() {
	add1 := func(value int, continuation func(int)) {
		continuation(value + 1)
	}

	mul5 := func(value int, continuation func(int)) {
		continuation(value * 5)
	}

	capture := new(capture[int])

	// prints 65
	withcc(capture, func(withccArg int) {
		add1(withccArg, func(add1Result int) {
			mul5(add1Result, func(mul5Result int) {
				fmt.Printf("%v\n", mul5Result)
			})
		})
	})(12)

	capture.recall(10) // prints 55
	capture.recall(3)  // prints 20
	capture.recall(4)  // prints 25
}
