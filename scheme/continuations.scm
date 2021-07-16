;(define add1 (lambda (n k) (k (+ 1 n))))
;(define mul2 (lambda (n k) (k (* 2 n))))

;-----

;(define lazy-add1
;  (lambda (n expr)
;    (let ((proc (eval expr (interaction-environment))))
;      (begin
;        (display expr)
;        (display "\n")
;      (proc (+ 1 n))))))
;
;(define lazy-mul2
;  (lambda (n expr)
;    (let ((proc (eval expr (interaction-environment))))
;      (begin
;        (display expr)
;        (display "\n")
;      (proc (* 2 n))))))
;
;(lazy-add1 13 '(lambda (a) (lazy-mul2 a '(lambda (b) b))))

;-----

;(define add1 (lambda (n k) (k (+ 1 n))))
;(define mul5 (lambda (n k) (k (* 5 n))))

;(define with-cc
;  (lambda (value expr continuation)
;    (begin
;      (expr continuation)
;      (continuation value))))
;
;(define first-continuation #f)
;(define second-continuation #f)
;(with-cc 10
;  (lambda (cont) (set! first-continuation cont))
;  (lambda (a)
;    (add1 a (lambda (b)
;              (begin
;                (with-cc b
;                  (lambda (cont) (set! second-continuation cont))
;                  (lambda (c) (mul5 c (lambda (d) d)))))))))
;(first-continuation 0)
;(second-continuation 3)

;(add1 10 (lambda (a) (mul5 a (lambda (b) b))))

;-----

;;;;;;;;
;; (add1 5 (lambda (n) (mul2 n (lambda (k) k))))
;; (lambda (n) (mul2 n (lambda (k) k))) is the "current continuation" of add1
;; (lambda (k) k) is the "current continuation" of mul2
;;;;;;;;

;-----

;; storing a continuation
(define x #f)

(* 5 (+ 1 (call-with-current-continuation
           (lambda (cont)
             (set! x cont)
             10))))

(x 4)
(x 3)

;(define x #f)
;(* 5 (+ 1 (call-with-current-continuation (lambda (cont) (begin (set! x cont) (cont 10) 6)))))
;(x 0)