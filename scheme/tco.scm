(define (fib-tco a b counter limit)
  (cond
    ((< limit counter) a)
    ((= counter limit) b)
    (else (fib-tco b (+ b a) (+ counter 1) limit))))

(define (fib-classic n)
  (cond
    ((= n 0) 0)
    ((= n 1) 1)
    (else
     (+ (fib-classic (- n 1))
        (fib-classic (- n 2))))))

(fib-tco 0 1 1 12)
(fib-classic 12)
