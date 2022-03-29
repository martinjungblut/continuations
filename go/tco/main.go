package main

import (
	"fmt"
	"math/big"
)

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

func fib(a *big.Int, b *big.Int, counter *big.Int, limit *big.Int) result[*big.Int] {
	zero, one := big.NewInt(0), big.NewInt(1)

	if limit.Cmp(zero) == 0 {
		return finalValue(zero)
	} else if counter.Cmp(limit) == 0 {
		return finalValue(b)
	} else {
		return nextContinuation(func() result[*big.Int] {
			return fib(b, a.Add(a, b), counter.Add(counter, one), limit)
		})
	}
}

func main() {
	fmt.Printf("%v\n", recurse(func() result[*big.Int] {
		a, b := big.NewInt(0), big.NewInt(1)
		counter := big.NewInt(1)
		limit := big.NewInt(2000)

		return fib(a, b, counter, limit)
	}))
}
