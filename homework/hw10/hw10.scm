(define (accumulate combiner start n term)
  (if (= n 0)
      start
      (combiner (term n) (accumulate combiner start (- n 1) term))
  )
)

(define (accumulate-tail combiner start n term)
  (define (accumulate-iter n result)
    (if (= n 0)
        result
        (accumulate-iter (- n 1) (combiner result (term n)))))
  (accumulate-iter n start)
)

(define-macro (list-of expr for var in seq . if-condition)
  `(map (lambda (,var) ,expr) (filter (lambda (,var) ,(car (cdr if-condition))) ,seq))
)