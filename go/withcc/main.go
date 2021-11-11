package main

import "fmt"

type continuation func(...interface{})

func (c *continuation) set(cont continuation) {
	*c = cont
}

func (c continuation) call(input ...interface{}) {
	if c != nil {
		c(input...)
	}
}

func NewCapture() *continuation {
	return new(continuation)
}

func withcc(capture *continuation, cont continuation) continuation {
	capture.set(cont)
	return cont
}

func main() {
	add1 := func(k func(...interface{}), args ...interface{}) {
		k(args[0].(int) + 1)
	}

	mul5 := func(k func(...interface{}), args ...interface{}) {
		k(args[0].(int) * 5)
	}

	firstCapture := NewCapture()

	// prints 65
	withcc(firstCapture, func(a ...interface{}) {
		add1(func(b ...interface{}) {
			mul5(func(c ...interface{}) {
				fmt.Printf("%v\n", c[0])
			}, b...)
		}, a...)
	})(12)

	firstCapture.call(10) // prints 55
	firstCapture.call(3)  // prints 20
	firstCapture.call(4)  // prints 25
}
