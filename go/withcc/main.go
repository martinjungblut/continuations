package main

import "fmt"

type continuation[T any] struct {
	f func(...T)
}

func (c continuation[T]) call(input ...T) {
	if c.f != nil {
		c.f(input...)
	}
}

func withcc[T any](c *continuation[T], f func(...T)) func(...T) {
	c.f = f
	return f
}

func main() {
	add1 := func(cont func(...int), args ...int) {
		cont(args[0] + 1)
	}

	mul5 := func(cont func(...int), args ...int) {
		cont(args[0] * 5)
	}

	firstCapture := new(continuation[int])

	// prints 65
	withcc[int](firstCapture, func(outerParams ...int) {
		add1(func(add1Results ...int) {
			mul5(func(mul5Results ...int) {
				fmt.Printf("%v\n", mul5Results[0])
			}, add1Results...)
		}, outerParams...)
	})(12)

	firstCapture.call(10) // prints 55
	firstCapture.call(3)  // prints 20
	firstCapture.call(4)  // prints 25
}
