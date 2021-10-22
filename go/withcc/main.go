package main

import "fmt"

type continuation func(interface{})

func withcc(capt *capture, cont continuation) continuation {
	capt.set(cont)
	return cont
}

type capture struct {
	captured continuation
}

func (c *capture) set(cont continuation) {
	c.captured = cont
}

func (c capture) call(input interface{}) {
	c.captured(input)
}

func main() {
	add1 := func(v interface{}, k func(interface{})) {
		k(v.(int) + 1)
	}

	mul5 := func(v interface{}, k func(interface{})) {
		k(v.(int) * 5)
	}

	capt := new(capture)

	withcc(capt, func(a interface{}) {
		add1(a, func(b interface{}) {
			mul5(b, func(c interface{}) {
				fmt.Printf("%v\n", c)
			})
		})
	})(12)

	capt.call(7)
}
