(menu-bar-mode -1)
(tool-bar-mode -1)
(scroll-bar-mode -1)

;https://i.imgur.com/6vYPb3C.jpg
(setq frame-inhibit-implied-resize t) ;; prevent resize window on startup
(setq default-frame-alist '((width . 100) (height . 35)))

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(custom-safe-themes
   '("cca1d386d4a3f645c2f8c49266e3eb9ee14cf69939141e3deb9dfd50ccaada79"
     default))
 '(org-format-latex-options
   '(:foreground default :background default :scale 2.0 :html-foreground
		 "Black" :html-background "Transparent" :html-scale
		 1.0 :matchers ("begin" "$1" "$" "$$" "\\(" "\\[")))
 '(package-selected-packages
   '(browse-kill-ring buffer-move casual clhs dash ein f flycheck fzf
		      lsp-mode lua-mode magit-section marginalia
		      modus-themes nodejs-repl paredit trashed vertico
		      zeal-at-point)))

(load-theme 'modus-vivendi t)

(global-set-key (kbd "M-n")
   "\261\C-v\C-n")

(global-set-key (kbd "M-p")
   "\255\261\C-v\C-p")


;(require 'expand-region)
;(global-set-key (kbd "C-=") 'er/expand-region)

(add-to-list 'package-archives '("melpa" . "http://melpa.org/packages/") t)


(require 'package)
(package-initialize)

(require 'nodejs-repl)

(add-hook 'js-mode-hook
              (lambda ()
                (define-key js-mode-map (kbd "C-x C-e") 'nodejs-repl-send-last-expression)
                (define-key js-mode-map (kbd "C-c C-j") 'nodejs-repl-send-line)
                (define-key js-mode-map (kbd "C-c C-r") 'nodejs-repl-send-region)
                (define-key js-mode-map (kbd "C-c C-c") 'nodejs-repl-send-buffer)
                (define-key js-mode-map (kbd "C-c C-l") 'nodejs-repl-load-file)
                (define-key js-mode-map (kbd "C-c C-z") 'nodejs-repl-switch-to-repl)))

(require 'clhs)
(setq clhs-root "file:///home/dio/hyperspec/")



(add-hook 'lisp-mode-hook
          (lambda ()
		    (local-set-key (kbd "C-c c") 'clhs-doc)))



(defun dio/gen-sequence-throwaway-name ()
  "create the list of strings from a to zz"
  (let ((seq '()))
    (dotimes (i 26)
      (push (char-to-string (+ ?a i)) seq))
    (dotimes (i 26)
      (dotimes (j 26)
	(push (concat (char-to-string (+ ?a i))
		      (char-to-string (+ ?a j)))
	      seq)))
    (reverse seq)))

(defun dio/find-throwaway-python (number)
  "create and open a throwaway python file; with prefix opens the last existing throwaway file"
  (interactive "p")
  (let ((seq (dio/gen-sequence-throwaway-name))
	(lastf ""))
    (catch 'foo
      (dolist (s seq)
	(let ((fname (concat s ".py")))
	  (if (= number 1)
	      (when (not (file-exists-p fname))
		(if (file-exists-p "a.py")
		    (progn
		      (find-file "a.py")
		      (set-visited-file-name fname))
		  (find-file fname))
		(throw 'foo nil))
	    (when (file-exists-p fname)
	      (setf lastf fname))))))
    (when (not (= number 1))
      (find-file lastf))))



(add-hook 'python-mode-hook
          (lambda ()
	    (local-set-key (kbd "C-c y") 'dio/find-throwaway-python)))


(add-hook 'org-mode-hook 'visual-line-mode)
(setq org-return-follows-link t)

(global-set-key (kbd "C-c e") 'eshell)
(global-set-key (kbd "C-c 0") 'bury-buffer)

(use-package zeal-at-point
  :ensure t
  :bind ("C-c d" . zeal-at-point)
  :config
;  (add-to-list 'zeal-at-point-mode-alist '(c-mode . "c"))
 ; (add-to-list 'zeal-at-point-mode-alist '(c++-mode . "cpp"))
  )



(recentf-mode 1)
(setq recentf-max-menu-items 125)
(setq recentf-max-saved-items 125)

(global-set-key (kbd "C-c r") 'recentf-open-files)

(global-set-key (kbd "C-c f") 'next-buffer)
(global-set-key (kbd "C-c b") 'previous-buffer)

(tab-bar-mode)
(global-set-key (kbd "C-c <left>") 'tab-bar-switch-to-prev-tab)
(global-set-key (kbd "C-c <right>") 'tab-bar-switch-to-next-tab)
(global-set-key (kbd "C-c <up>") 'tab-bar-new-tab)
(global-set-key (kbd "C-c <down>") 'tab-bar-close-tab)

(defun dio/find-previous-python ()
  "finds the lastly visited python buffer"
  (let ((recent-buffer nil)
	(recent-time 0)
	ret)
    (dolist (buffer (buffer-list) ret)
      (when (and (not ret) 
		 (string-suffix-p ".py" (buffer-name buffer) t))
	(setq ret (buffer-name buffer))))
    ret))

(global-set-key (kbd "C-c p") 
		(lambda () (interactive)
		  (if (get-buffer "*Python*")
		      (if (equal "*Python*" (buffer-name (current-buffer)))
			  (let ((py (dio/find-previous-python)))
			    (when py 
			      (switch-to-buffer py)))
			(switch-to-buffer "*Python*"))
		    (run-python)
		    (switch-to-buffer "*Python*"))))

(global-set-key (kbd "C-c l")
		(lambda () (interactive)
		  (switch-to-buffer "*scratch*")))
(global-set-key (kbd "C-c o")
		(lambda () (interactive)
		  (find-file-at-point)))

(global-set-key (kbd "C-c aa") (lambda () (interactive) (find-file "~/org/about.org")))
(global-set-key (kbd "C-c af") (lambda () (interactive) (find-file "~/org/phi.org")))
(global-set-key (kbd "C-c ae") (lambda () (interactive) (find-file "~/.emacs")))
(global-set-key (kbd "C-c av") (lambda () (interactive) (find-file "~/.vimrc")))
(global-set-key (kbd "C-c ac") 'org-capture)
(global-set-key (kbd "C-c ap") (lambda () (interactive) 
                                 (cd "~/test")
                                 (run-python) 
                                 (delete-other-windows)
                                 (split-window-below)
                                 (find-file "~/test/test.py")))

(global-set-key (kbd "C-c as") (lambda () (interactive) (scratch-buffer)))

(global-set-key (kbd "C-c al") (lambda () (interactive) 
                                 (cd "~/test")
                                 (let ((b (get-buffer "*slime-repl sbcl*")))
                                   (if b
                                       (switch-to-buffer b)
                                       (slime))) 
                                 (delete-other-windows)
                                 (split-window-below)
                                 (find-file "~/test/test.lsp")))


(global-set-key (kbd "C-c am") (lambda () (interactive) 
                                 (cd "~/test/lisp/lisp-adventure/")
                                 (let ((b (get-buffer "*slime-repl sbcl*")))
                                   (if b
                                       (switch-to-buffer b)
                                       (slime))) 
                                 (delete-other-windows)
                                 (split-window-below)
                                 (find-file "~/test/lisp/lisp-adventure/main.lsp")))


(global-set-key (kbd "C-c at") 
                (lambda () 
                  (interactive) 
                  (find-file "~/read/misc/tractatus-logico-org-master/tractatus.org")))



(set-face-attribute 'default nil :height 140)


;(add-hook 'python-mode-hook 'py-autopep8-mode)
(add-hook 'python-mode-hook 'electric-pair-mode)
(add-hook 'c-mode-hook 'electric-pair-mode)
;(add-hook 'elpy-mode-hook 'py-autopep8-mode)
;(add-hook 'elpy-mode-hook 'electric-pair-mode)

(add-hook 'slime-repl-mode-hook 'electric-pair-mode)
(add-hook 'slime-repl-mode-hook 'enable-paredit-mode)
(add-hook 'lisp-mode-hook 'electric-pair-mode)
(add-hook 'c++-mode-hook 'electric-pair-mode)
(add-hook 'js-mode-hook 'electric-pair-mode)


(setq inferior-lisp-program "sbcl")

(autoload 'enable-paredit-mode "paredit" "turn on pseudo-structural editing of lisp code" t)
(add-hook 'ielm-mode-hook #'enable-paredit-mode)
(add-hook 'lisp-mode-hook #'enable-paredit-mode)
(add-hook 'scheme-mode-hook #'enable-paredit-mode)
(add-hook 'emacs-lisp-mode-hook #'enable-paredit-mode)

(add-hook 'lisp-interaction-mode-hook
          (lambda ()
            (keymap-set lisp-interaction-mode-map "C-c C-c" 'eval-print-last-sexp)))

(setq-default c-basic-offset 4)



;; You need to modify the following line
(setq load-path (cons "~/test/lean/lean4-mode" load-path))

(setq lean4-mode-required-packages '(dash f flycheck lsp-mode magit-section s))

(let ((need-to-refresh t))
  (dolist (p lean4-mode-required-packages)
    (when (not (package-installed-p p))
      (when need-to-refresh
        (package-refresh-contents)
        (setq need-to-refresh nil))
      (package-install p))))

(require 'lean4-mode)
(put 'narrow-to-region 'disabled nil)


(global-set-key (kbd "<mouse-2>") 'clipboard-yank)

(add-to-list 'auto-mode-alist '("\\.ino\\'" . c-mode))

(add-to-list 'c-default-style '(c-mode . "k&r"))
(setq indent-tabs-mode nil)
(delete-selection-mode 1)


(require 'casual)
(define-key calc-mode-map (kbd "C-o") 'casual-main-menu)

(require 'buffer-move)

(defun ab/switch-buffer-each-other (arg)
  "switch current buffer with other window buffer 
   right-2-left and up-2-down"
  (interactive "p")
  (cond
   ((windmove-find-other-window 'right) (buf-move-right))
   ((windmove-find-other-window 'left) (buf-move-left))
   ((windmove-find-other-window 'up) (buf-move-up))
   ((windmove-find-other-window 'down) (buf-move-down)))
  (message "switch buffer done"))

(defvar dio/inc-x 0)
(defvar dio/inc-sign 1)

(defun dio/inc (arg) 
  (interactive "p")
  (cond 
   ((< arg 0)
    (setq dio/inc-x (- arg))
    (setq dio/inc-sign -1))
   ((> arg 1)
    (setq dio/inc-x arg)
    (setq dio/inc-sign 1))
   ((= arg 0)
    (setq dio/inc-x 0)
    (setq dio/inc-sign 1))
   ((= arg 1)
    (setq dio/inc-x (+ dio/inc-x dio/inc-sign))))
  (insert (format "%d" dio/inc-x)))

(global-set-key (kbd "C-c +") 'dio/inc)

(global-set-key (kbd "C-c s") 'ab/switch-buffer-each-other)


   
(put 'downcase-region 'disabled nil)
(put 'upcase-region 'disabled nil)


;; by default it's t, meaning all warnings; this inhibits lots 
(setq byte-compile-warnings '(cl-functions))

;; no splash

(setq inhibit-splash-screen t)
(require 'browse-kill-ring)
(browse-kill-ring-default-keybindings)
(global-set-key (kbd "C-c k") 'browse-kill-ring)

(put 'dired-find-alternate-file 'disabled nil)

;; prot dired mode configs

; vertical minibuffer (package vertigo)
(setq vertico-resize nil)
(vertico-mode 1)

;side notes to M-x, M-: function calls and other stuff (package marginalia)
(marginalia-mode 1)


; able to type paths directly ignoring current
(file-name-shadow-mode 1)
; when you do that, clean former
(add-hook 'rfn-eshadow-update-overlay-hook #'vertico-directory-tidy)


; (package trashed)
(setq delete-by-moving-to-trash t)

(setq dired-dwim-target t)
(add-hook 'dired-mode-hook #'dired-hide-details-mode)


(add-hook 'dired-mode-hook (lambda () (dired-omit-mode)))

(setq backup-by-copying t)

(require 'dired)
(define-key dired-mode-map (kbd "% /") 'dired-mark-directories)
(define-key dired-mode-map (kbd "% *") 'dired-mark-executables)
(define-key dired-mode-map (kbd "% .") 'dired-mark-extension)




(setq dired-listing-switches "-al") ; if you want to include the hidden files from dired
;(setq dired-listing-switches "-l") ; if you want to remove the hidden files from dired



; C-c C-= and C-c C-- increase and decrease the global font height
; with zero parameter reset to default
; with positive parm repeat more times 
(defvar *dio/face-height-default* 140)
(defvar *dio/face-height* *dio/face-height-default*)
(set-face-attribute 'default nil :height *dio/face-height*)
(global-set-key (kbd "C-c C-=")
		(lambda (arg)
		  (interactive "p")
                  (if (> arg 0)
                      (dotimes (x (min 19 (max arg 1)))
		        (setf *dio/face-height* (+ (if (> *dio/face-height* 100) 20 10) *dio/face-height*)))
                    (setf *dio/face-height* *dio/face-height-default*))
                  (set-face-attribute 'default nil :height *dio/face-height*)
                  (text-scale-adjust 0)))

(global-set-key (kbd "C-c C--")
		(lambda (arg)
		  (interactive "p")
                  (if (> arg 0)
                      (dotimes (x (min 19 (max arg 1)))
		        (setf *dio/face-height* 
                              (- *dio/face-height*
                                 (cond
                                  ((< *dio/face-height* 20) 0)
                                  ((< *dio/face-height* 100) 10)
                                  (t 20)))))
                    (setf *dio/face-height* *dio/face-height-default*))
		  (set-face-attribute 'default nil :height *dio/face-height*)
                  (text-scale-adjust 0)))



(add-to-list 'default-frame-alist '(alpha-background . 85))

(setq org-directory "~/org/")
(setq org-default-notes-file (concat org-directory "/notes.org"))

(setq org-capture-templates
      '(("p" "philosophy stuffs")
	("pa" "ask question" entry (file+headline "phi.org" "Question")
	 "* %? %i\n")
	("pj" "joke" entry (file+headline "~/org/phi.org" "Joke") "* %? %i\n")
	("pu" "Unsinn" entry (file+headline "~/org/phi.org" "Nonsense") "* %? %i\n")
	("pb" "bookmark" entry (file+headline "phi.org" "Bookmark") "* %? %i\n")
	("ps" "quotation" entry (file+headline "phi.org" "Quotation") "* %? %i\n")

	("b" "band" plain (file+olp "about.org" "listen" "new stuff") 
	 "   %? %^{genre|:death:|:black:|:thrash:|:folk:|:viking:|:power metal:|:speed:}\n")
	("t" "Todo" entry (file+headline "~/org/gtd.org" "Tasks")
         "* TODO %?\n  %i\n  %a")
        ("j" "Journal" entry (file+datetree "~/org/journal.org")
         "* %?\nEntered on %U\n  %i\n  %a")
	("r" "rent" entry (file+olp "about.org" "misc" "rent")
	 "* %U\n %?\n")
))

(put 'scroll-left 'disabled nil)


(put 'set-goal-column 'disabled nil)
(global-set-key (kbd "C-x h") 'help)
