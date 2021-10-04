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

(define add1 (lambda (n k) (k (+ 1 n))))
(define mul5 (lambda (n k) (k (* 5 n))))

(define with-cc
  (lambda (capture-continuation continuation)
    (begin
      (capture-continuation continuation)
      continuation)))

(define captured-continuation #f)

((with-cc
    (lambda (cont) (set! captured-continuation cont))
  (lambda (a)
    (add1 a (lambda (b) (mul5 b (lambda (c) (display c))))))) 10)

;-----

;;;;;;;;
;; (add1 5 (lambda (n) (mul2 n (lambda (k) k))))
;; (lambda (n) (mul2 n (lambda (k) k))) is the "current continuation" of add1
;; (lambda (k) k) is the "current continuation" of mul2
;;;;;;;;

;-----

;; storing a continuation
;(define x #f)

;(* 5 (+ 1 (call-with-current-continuation
;           (lambda (cont)
;             (set! x cont)
;             10))))

;(x 4)
;(x 3)

;(define x #f)
;(* 5 (+ 1 (call-with-current-continuation (lambda (cont) (begin (set! x cont) (cont 10) 6)))))
;(x 0)

;(define x #f)  ; 'x' will hold the result of squaring 10
;
;(define square  ; square a number, uses continuation-passing style
;  (lambda (v k)
;    (k (* v v))))
;
;(define capture  ; capture sets 'x' to the value of 'm'
;  (lambda (m)
;    (set! x m)))
;
;(square 10 capture)
;(= x 100)