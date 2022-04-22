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

func factorial(n *big.Int, acc *big.Int) result[*big.Int] {
	zero, one := big.NewInt(0), big.NewInt(1)

	if acc == nil {
		acc = big.NewInt(1)
	}

	if n.Cmp(zero) == 0 || n.Cmp(one) == 0 {
		return finalValue(acc)
	} else {
		return nextContinuation(func() result[*big.Int] {
			return factorial(new(big.Int).Sub(n, one), acc.Mul(acc, n))
		})
	}
}

func main() {
	fmt.Printf("%v\n", recurse(func() result[*big.Int] {
		n := big.NewInt(5)
		return factorial(n, nil)
	}))
}
