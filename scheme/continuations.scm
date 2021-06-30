(define fibonacci
  (lambda (a b counter limit)
    (if (= counter limit) b
        (fibonacci b (+ a b) (+ 1 counter) limit))))

(define fib
  (lambda (n)
    (fibonacci 0 1 1 n)))

;; (fib 10)

(define add1
  (lambda (n k)
    (k (+ 1 n))))

(define mul2
  (lambda (n k)
    (k (* 2 n))))

(add1 5 (lambda (n) (mul2 n (lambda (k) k))))
;; (lambda (n) (mul2 n (lambda (k) k))) is the "current continuation" of add1
;; (lambda (k) k) is the "current continuation" of mul2

;(define x #f)
;
;(* 5 (+ 1 (call-with-current-continuation
;        (lambda (cont)
;          (set! x cont)
;          10))))
;
;(x 4)