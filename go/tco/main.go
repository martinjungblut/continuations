package main

import "fmt"

type continuation[T any] func() result[T]

type result[T any] struct {
	value        T
	continuation *continuation[T]
}

func recurse[T any](continuation continuation[T]) T {
	result := continuation()
	for {
		if result.continuation != nil {
			result = (*result.continuation)()
		} else {
			break
		}
	}
	return result.value
}

func nextContinuation[T any](continuation continuation[T]) result[T] {
	return result[T]{continuation: &continuation}
}

func finalValue[T any](value T) result[T] {
	return result[T]{value: value}
}

func fib(a uint64, b uint64, counter uint64, limit uint64) result[uint64] {
	if limit == 0 {
		return finalValue(uint64(0))
	} else if counter < limit {
		return nextContinuation(func() result[uint64] {
			return fib(b, a+b, counter+1, limit)
		})
	} else {
		return finalValue(b)
	}
}

func main() {
	fmt.Printf("%v\n", recurse(func() result[uint64] {
		return fib(0, 1, 1, 2000)
	}))
}
