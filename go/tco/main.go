package main

import "fmt"

type capture[T any] struct {
	continuation func() optional[T]
}

type optional[T any] struct {
	value   T
	capture *capture[T]
}

func recurse[T any](c func() optional[T]) T {
	result := c()
	for {
		if result.capture != nil {
			result = result.capture.continuation()
		} else {
			break
		}
	}
	return result.value
}

func fib(a uint64, b uint64, counter uint64, limit uint64) optional[uint64] {
	if limit == 0 {
		return optional[uint64]{value: 0}
	} else if counter < limit {
		return optional[uint64]{capture: &capture[uint64]{
			func() optional[uint64] {
				return fib(b, a+b, counter+1, limit)
			},
		}}
	} else {
		return optional[uint64]{value: b}
	}
}

func main() {
	fmt.Printf("%v\n", recurse(func() optional[uint64] {
		return fib(0, 1, 1, 2000)
	}))
}
