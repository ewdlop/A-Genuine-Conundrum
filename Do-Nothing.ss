(define (trolley-problem track-main track-alt)
  (display "Decision time: Do you 'saveGroup' or 'saveIndividual'? Type 'exit' to quit.\n")
  (let ((decision (read))) ; Read user input
    (cond
      [(equal? decision 'saveGroup)
       (begin
         (display (string-append "Switching to alternative track. "
                                 (number->string track-alt) " person(s) sacrificed.\n"))
         (trolley-problem track-main track-alt))] ; Recursive call
      [(equal? decision 'saveIndividual)
       (begin
         (display (string-append "Staying on the main track. "
                                 (number->string track-main) " person(s) sacrificed.\n"))
         (trolley-problem track-main track-alt))] ; Recursive call
      [(equal? decision 'exit)
       (display "Exiting the trolley problem. Goodbye!\n")]
      [else
       (begin
         (display "Invalid decision. Please try again.\n")
         (trolley-problem track-main track-alt))]))) ; Recursive call for invalid input

;; Example Usage
(trolley-problem 5 1)
