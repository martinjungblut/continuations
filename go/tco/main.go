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

type continuation[T any] struct {
	funcref func(...T) continuation[T]
	args    []T
}

func NewContinuation(funcref func(...interface{}) continuation, args ...interface{}) continuation {
	return continuation{funcref, args}
}

type capture struct {
	called bool
	values []interface{}
}

func continuationFib(args ...interface{}) continuation {
	a := args[0].(uint64)
	b := args[1].(uint64)
	counter := args[2].(uint64)
	limit := args[3].(uint64)
	doCapture := args[4].(func(...interface{}) continuation)

	if counter > limit {
		return NewContinuation(doCapture, a)
	} else if counter == limit {
		return NewContinuation(doCapture, b)
	} else {
		return NewContinuation(continuationFib, b, a+b, counter+1, limit, doCapture)
	}
}

func improvedFib(a uint64, b uint64, counter uint64, limit uint64) uint64 {
	capture := new(capture)

	doCapture := func(values ...interface{}) continuation {
		capture.called = true
		capture.values = values
		return continuation{}
	}

	nextContinuation := continuationFib(a, b, counter, limit, doCapture)
	for !capture.called {
		nextContinuation = nextContinuation.funcref(nextContinuation.args...)
	}

	return capture.values[0].(uint64)
}

func main() {
	// fmt.Printf("%v\n", classicFib(0, 1, 1, 8_000_000))
	fmt.Printf("%v\n", improvedFib(0, 1, 1, 8_000_000))
}
