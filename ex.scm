(define (repeat k fn)
    (if (> k 1)
        (begin (fn) (repeat (- k 1) fn))
        (fn)))

(define (tri fn)
    (repeat 3 (lambda () (fn) (lt 120))))

(define (sier d k)
    (tri (lambda ()
            (if (= k 1) (fd d)
                (leg d k)))))

(define (leg d k)
    (sier (/ d 2) (- k 1))
    (penup)
    (fd d)
    (pendown))

(define (range a b)
    (if (>= a b)
        nil
        (cons a (range (+ a 1) b))))

(define (int-stream start)
    (cons-stream start (int-stream (+ start 1))))

(define (prefix s k)
    (if (= k 0)
        ()
        (cons (car s) (prefix (cdr-stream s) (- k 1)))))

(define (square-stream s)
    (cons-stream (* (car s) (car s))
                 (square-stream (cdr-stream s))))

(define (map-stream f s)
    (if (null? s)
        nil
        (cons-stream (f (car s))
                     (map-stream f (cdr-stream s)))))

(define (filter-stream f s)
    (if (null? s)
        nil
        (if (f (car s))
            (cons-stream (car s) (filter-stream f (cdr-stream s)))
            (filter-stream f (cdr-stream s)))))

(define (sieve s)
    (cons-stream (car s)
                 (sieve
                    (filter-stream
                        (lambda (x) (not (= 0 (remainder x (car s)))))
                        (cdr-stream s)))))

(define primes (sieve (int-stream 2)))

(define (fib n)
    (if (<= n 1)
        n
        (+ (fib (- n 2)) (fib (- n 1)))))

(define (fib-exp n)
    (if (<= n 1)
        n
        (list '+ (fib-exp (- n 2)) (fib-exp (- n 1)))))

(define-macro (twice expr)
    (list 'begin expr expr))

(define-macro (for sym vals expr)
    (list 'map (list 'lambda (list sym) expr) vals))