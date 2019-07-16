(define (find s predicate)
  (if (null? s)
    #f
    (if (predicate (car s))
    (car s)
    (find (cdr-stream s) predicate)))
)

(define (scale-stream s k)
  (if (null? s)
    nil
    (cons-stream (* k (car s)) (scale-stream (cdr-stream s) k)))
)

(define (has-cycle s)
  (define (helper so-far cur)
    (cond ((null? cur) #f)
      ((contains so-far cur) #t)
      (else (helper (cons cur so-far) (cdr-stream cur)))))
  (helper nil s)
)

;;; Is lst contains cur?
;;; This function works not only on stream, but all list
(define (contains lst cur)
    (cond ((null? lst) #f)
      ((eq? cur (car lst)) #t)
      (else (contains (cdr lst) cur))))


;;; https://www.studocu.com/en-au/document/university-of-california-berkeley/the-structure-and-interpretation-of-computer-progra/other/homework-11-solutions-cs-61a-spring-2018/1702843/view
;;; Complete explanation can be found in the above page.
(define (has-cycle-constant s)
  (define (helper slow fast)
    (cond ((or (null? fast) (null? (cdr-stream fast))) #f)
      ((eq? slow fast) #t)
      (else (helper (cdr-stream slow) (cdr-stream (cdr-stream fast))))))  

  (helper s (cdr-stream s))
)


