package main

import "fmt"

type continuation func(interface{})

func (c *continuation) set(cont continuation) {
	*c = cont
}

func (c continuation) call(input interface{}) {
	if c != nil {
		c(input)
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
	add1 := func(v interface{}, k func(interface{})) {
		k(v.(int) + 1)
	}

	mul5 := func(v interface{}, k func(interface{})) {
		k(v.(int) * 5)
	}

	capture := NewCapture()

	withcc(capture, func(a interface{}) {
		add1(a, func(b interface{}) {
			mul5(b, func(c interface{}) {
				fmt.Printf("%v\n", c)
			})
		})
	})(12)

	capture.call(10)
	capture.call(3)
	capture.call(4)

	fmt.Println("-----")

	scapture := NewCapture()

	add1(3, withcc(scapture, func(b interface{}) {
		mul5(b, func(c interface{}) {
			fmt.Printf("%v\n", c)
		})
	}))

	scapture.call(10)
}
