package main

import (
	"fmt"
	"math/big"
)

type result[T any] struct {
	value        T
	continuation func() result[T]
}

func recurse[T any](continuation func() result[T]) T {
	result := continuation()
	for result.continuation != nil {
		result = result.continuation()
	}
	return result.value
}

func nextContinuation[T any](continuation func() result[T]) result[T] {
	return result[T]{continuation: continuation}
}

func finalValue[T any](value T) result[T] {
	return result[T]{value: value}
}

func factorial(n *big.Int, acc *big.Int) func() result[*big.Int] {
	return func() result[*big.Int] {
		zero, one := big.NewInt(0), big.NewInt(1)

		if acc == nil {
			acc = one
		}

		if n.Cmp(zero) == 0 || n.Cmp(one) == 0 {
			return finalValue(acc)
		} else {
			return nextContinuation(factorial(new(big.Int).Sub(n, one), acc.Mul(acc, n)))
		}
	}
}

func main() {
	fmt.Printf("%v\n", recurse(factorial(big.NewInt(125000), nil)))
}
