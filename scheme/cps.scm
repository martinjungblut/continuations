(define add1 (lambda (n k) (k (+ 1 n))))

(define work1
  (lambda (w1)
    (add1 w1 work2)))

(define work2
  (lambda (w2)
    (add1 w2 identity)))

(define identity
  (lambda (c) c))

;; (add1 3 (lambda (a) (add1 a (lambda (b) (add1 b (lambda (c) c))))))
(add1 3 work1)