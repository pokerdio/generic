
(defmacro global-set-keys (&rest args)
  "Bind multiple keys globally.
Takes a flat list of key-function or key-file-path pairs"
  (unless (cl-evenp (length args))
    (error "global-set-keys: must supply key function pairs"))
  `(progn
     ,@(cl-loop for (key fn) on args by #'cddr
                collect `(global-set-key (kbd ,key) 
					 ,(cond ((stringp fn) 
						 `(lambda () (interactive)
						    (find-file ,fn)))
						((consp fn) fn)
						((symbolp fn) `#',fn))))))

(defmacro buf-sw (name)
  `(lambda () (interactive) (switch-to-buffer ,name)))

(defmacro mode-set-keys (map-list &rest args)
  "Bind multiple keys in MODE's keymap.
Takes a flat list of key-function pairs."
  (unless (cl-evenp (length args))
    (error "mode-set-keys: must supply key/function pairs"))
  (when (not (listp map-list))
    (setf map-list (list map-list)))
  `(progn
     ,@ (cl-loop for m in map-list append
		 (progn
		   (when (not (boundp m))
		     (error "could not find key map %s" m))
		   (cl-loop for (key fn) on args by #'cddr
			    collect `(keymap-set ,m ,key #',fn))))))

(defun my/macroexpand-1-at-point (&optional to-scratch)
  "Macroexpand-1 the form at point.
If TO-SCRATCH is non-nil (e.g. via prefix argument), insert result in *scratch*.
Otherwise, show the result in the minibuffer via `message`."
  (interactive "P")
  (let ((form (sexp-at-point))
        (result))
    (unless form
      (user-error "No form found at point"))
    (setq result (macroexpand-1 form))
    (if to-scratch
	(message "%s" (pp-to-string result))
      (let ((scratch (scratch-buffer)))
	(switch-to-buffer scratch)
	(with-current-buffer scratch
	  (goto-char (point-max))
	  (insert "\n;; macroexpand-1 result:\n"
		  (pp-to-string result)))))))


(defun my/macroexpand-at-point (&optional to-scratch)
  "Macroexpand the form at point.
If TO-SCRATCH is non-nil (e.g. via prefix argument), insert result in *scratch*.
Otherwise, show the result in the minibuffer via `message`."
  (interactive "P")
  (let ((form (sexp-at-point))
        (result))
    (unless form
      (user-error "No form found at point"))
    (setq result (macroexpand form))
    (if to-scratch
	(message "%s" (pp-to-string result))
      (let ((scratch (scratch-buffer)))
	(switch-to-buffer scratch)
	(with-current-buffer scratch
	  (goto-char (point-max))
	  (insert "\n;; macroexpand-1 result:\n"
		  (pp-to-string result)))))))

