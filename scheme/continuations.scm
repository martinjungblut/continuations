(define add1 (lambda (n k) (k (+ 1 n))))
(define mul2 (lambda (n k) (k (* 2 n))))

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

(define evaluate
  (lambda (expr)
    (eval expr (interaction-environment))))

(define lazy-add1
  (lambda (n expr)
    (let ((continuation (evaluate expr)))
      (lambda args
        (if (>= (length args) 1)
            (continuation (+ 1 (car args)))
            (continuation (+ 1 n)))))))

(define lazy-mul2
  (lambda (n expr)
    (let ((continuation (evaluate expr)))
      (lambda args
        (if (>= (length args) 1)
            (continuation (* 2 (car args)))
            (continuation (* 2 n)))))))

(((lazy-add1 13 '(lambda (a) (lazy-mul2 a '(lambda (b) b))))))

;-----

;;;;;;;;
;; (add1 5 (lambda (n) (mul2 n (lambda (k) k))))
;; (lambda (n) (mul2 n (lambda (k) k))) is the "current continuation" of add1
;; (lambda (k) k) is the "current continuation" of mul2
;;;;;;;;

;-----

;; storing a continuation
;(define x #f)
;
;(* 5 (+ 1 (call-with-current-continuation (lambda (cont) (set! x cont) 10))))
;
;(x 4)

;(define x #f)
;(* 5 (+ 1 (call-with-current-continuation (lambda (cont) (begin (set! x cont) (cont 10) 6)))))
;(x 0)