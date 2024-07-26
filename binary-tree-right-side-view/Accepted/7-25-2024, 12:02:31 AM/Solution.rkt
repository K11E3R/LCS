// https://leetcode.com/problems/binary-tree-right-side-view

; Definition for a binary tree node.
#|

; val : integer?
; left : (or/c tree-node? #f)
; right : (or/c tree-node? #f)
(struct tree-node
  (val left right) #:mutable #:transparent)

; constructor
(define (make-tree-node [val 0])
  (tree-node val #f #f))

|#
(define (get-layer level [queue '()])
  (if (empty? level)
      queue
      (match (first level)
        [(tree-node a #f #f)
         (get-layer (rest level) queue)]
        [(tree-node a b #f)
         (get-layer (rest level) (append queue (list b)))]
        [(tree-node a #f b)
         (get-layer (rest level) (append queue (list b)))]
        [(tree-node a b c)
         (get-layer (rest level)
                    (append queue (list b c)))])))

(define (iter-layers initial [results '()])
  (if (eq? initial '())
      results
      (let ([res (get-layer initial)])
        (if (empty? res)
            (reverse results)
            (iter-layers res (cons (tree-node-val (last res)) results))))))

(define (right-side-view root)
  (if (not (tree-node? root))
      '()
      (cons (tree-node-val root)
        (iter-layers (list root)))))