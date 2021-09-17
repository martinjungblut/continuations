(define math
  (lambda (a b k)
    (k (+ a b))
    (k (- a b))
    (k (* a b))
    (k (/ a b))))

(define puts
  (lambda (x)
    (display x)
    (display "\n")))

;; 'math' is kept on the stack since it continues executing, TCO doesn't kick in
;; (math 10 5 puts)

(define add1 (lambda (a continue) (continue (+ a 1))))
(define sub1 (lambda (a continue) (continue (- a 1))))
(define continue-sub1 (lambda (x) (puts x)))
(define continue-add1 (lambda (x) (sub1 x continue-sub1)))

(define plus1 (lambda (a) (+ 1 a)))

(plus1 (plus1 (plus1 5)))

;(add1 5 continue-add1)