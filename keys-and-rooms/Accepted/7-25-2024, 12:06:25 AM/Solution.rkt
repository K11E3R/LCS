// https://leetcode.com/problems/keys-and-rooms

(define (can-visit-all-rooms rooms)
  (let ([seen-rooms (make-hash '((0 1)))])
    (define (dfs room)
      (map (λ (key)
             (if (hash-has-key? seen-rooms key)
                 #f
                 (begin
                   (hash-update! seen-rooms key add1 0)
                   (dfs (list-ref rooms key)))))
           room))
    (begin
      (dfs (first rooms))
      (= (hash-count seen-rooms)
         (length rooms)))))