package main

import "fmt"

type continuation func(interface{})

func withcc(capture func(continuation), cont continuation) continuation {
	capture(cont)
	return cont
}

func main() {
	var cont continuation = nil

	capture := func(m continuation) {
		cont = m
	}

	add1 := func(v interface{}, k func(interface{})) {
		k(v.(int) + 1)
	}

	mul5 := func(v interface{}, k func(interface{})) {
		k(v.(int) * 5)
	}

	withcc(capture, func(a interface{}) {
		add1(a, func(b interface{}) {
			mul5(b, func(c interface{}) {
				fmt.Printf("%v\n", c)
			})
		})
	})(10)

	cont(7)
}
