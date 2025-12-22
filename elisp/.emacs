;; Minimal for Lisp development

(setq inhibit-startup-message t)        ;; No splash screen
(menu-bar-mode -1)
(tool-bar-mode -1)
(scroll-bar-mode -1)
(global-display-line-numbers-mode t)
(add-to-list 'load-path (expand-file-name "lisp/" user-emacs-directory))
(load "dio-util")

;; Package setup
(require 'package)
(setq package-archives
      '(("gnu" . "https://elpa.gnu.org/packages/")
	("melpa-stable" . "https://stable.melpa.org/packages/")
	("melpa" . "https://melpa.org/packages/")))

(package-initialize)
(unless package-archive-contents
  (package-refresh-contents))

;; Use-package for easier config management
(unless (package-installed-p 'use-package)
  (package-install 'use-package))
(require 'use-package)
(setq use-package-always-ensure t)
(setq use-package-verbose t)


(use-package paredit
  :hook ((emacs-lisp-mode lisp-mode lisp-data-mode) . paredit-mode))

(use-package rainbow-delimiters
  :hook (prog-mode . rainbow-delimiters-mode))

(use-package sly
  :init
  (setq inferior-lisp-program "/usr/bin/sbcl"))

(with-eval-after-load 'sly
    (define-key sly-mode-map (kbd "C-c a r") #'sly-restart-inferior-lisp))

(with-eval-after-load 'sly-mrepl
  (define-key sly-mrepl-mode-map (kbd "C-c a r") #'sly-restart-inferior-lisp))

(use-package company
  :init (global-company-mode))

(use-package helpful
  :bind
  (("C-h f" . helpful-callable)
   ("C-h v" . helpful-variable)
   ("C-h k" . helpful-key)
   ("C-h x" . helpful-command)))

(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(doom-modeline-always-show-macro-register t)
 '(doom-modeline-enable-word-count t)
 '(doom-modeline-total-line-number t)
 '(package-selected-packages
   '(devdocs elpy vundo auctex magit treemacs-projectile which-key consult-projectile embark-consult embark marginalia orderless vertico doom-modeline projectile browse-kill-ring catppuccin-theme doom-themes sly-mrepl sly rainbow-delimiters paredit helpful company)))


(use-package doom-themes
  :config
  (load-theme 'doom-dracula :no-confirm)
  (setq doom-themes-enable-bold t
	doom-themes-enable-italic t))

;; (use-package catppuccin-theme
;;   :config
;;   (load-theme 'catppuccin :no-confirm))

(setq-default line-spacing 0.2)
(setq line-number-mode nil)

;; (set-frame-font "JetBrains Mono 16" nil t)

(when (member "Fira Code" (font-family-list))
  (set-frame-font "Fira Code Retina 14" t)
  (add-hook 'prog-mode-hook
            (lambda () (setq prettify-symbols-alist
                             '(("lambda" . ?λ)
                               ("->" . ?→)
                               ("=>" . ?⇒)))
              (prettify-symbols-mode 1))))

;; (set-frame-parameter (selected-frame) 'alpha-background 90)
;; (add-to-list 'default-frame-alist '(alpha-background . 90))

(defun open-init-file ()
  (interactive)
  (find-file user-init-file))

(use-package browse-kill-ring
  :bind (("C-c a k" . browse-kill-ring)))



(defun my/insert-indexed (nl count fmt)
  "Insert COUNT+1 lines using FMT, with index 0..COUNT.
FMT should contain a %d placeholder for the index."
  (interactive "p\nnCount: \nsFormat str: ")
  ;; (insert (format "%S %S %S\n" nl count fmt))
  (let ((i0 (if (<= 0 nl) nl (- -1 nl))))
    (setf nl (if (<= 0 nl) "\n" "")) 
    (dotimes (i (1+ (1- count)))
      (insert (format fmt (+ i i0)) nl))))

(global-set-keys 
 "C-c 1" my/macroexpand-1-at-point
 "C-c 2" my/macroexpand-at-point
 "C-c 3" my/insert-indexed
 "s-x" "~/org/xxx.org"
 "C-c a e" open-init-file
 "C-c a l" scratch-buffer
;; "C-c p" this is used by projectile
 "C-c e" eshell
 "C-c a p" package-list-packages
 "C-c a m" (buf-sw "*Messages*")
 "C-c a a" "~/org/about.org"
 "C-c a t" "~/org/tractatus-logico-org/tractatus.org"
 "C-c 0" bury-buffer)

(mode-set-keys (lisp-mode-shared-map lisp-interaction-mode-map)
	       "C-c C-j" eval-print-last-sexp)

(add-hook 'org-mode-hook #'visual-line-mode)


;; (use-package helm
;;   :ensure t
;;   :config
;;   (helm-mode 1)  ;; enable helm-mode globally

;;   ;; Replace built-ins with helm versions
;;   (global-set-key (kbd "M-x") 'helm-M-x)
;;   (global-set-key (kbd "C-x C-f") 'helm-find-files)
;;   (global-set-key (kbd "C-x b") 'helm-mini)
;;   (global-set-key (kbd "M-y") 'helm-show-kill-ring)
;;   (global-set-key (kbd "C-h a") 'helm-apropos)

;;   ;; Optional: fuzzy matching
;;   (setq helm-M-x-fuzzy-match t
;;         helm-buffers-fuzzy-matching t
;;         helm-recentf-fuzzy-match t))

(use-package projectile
  :ensure t
  :init
  (projectile-mode +1)
  :bind (:map projectile-mode-map 
	      ("C-c p" . projectile-command-map))
  :config
  (setq projectile-completion-system 'default))

;; Optional: helm-projectile (if you're using projectile)
;; (use-package helm-projectile
;;   :after (helm projectile)
;;   :config
;;   (helm-projectile-on))

;; Optional: live grep with helm-rg (if you install ripgrep)
;; (use-package helm-rg
;;   :after helm)

(global-auto-revert-mode t)

(setq backup-directory-alist `(("." . "~/.emacs.d/backups"))
      auto-save-file-name-transforms `((".*" "~/.emacs.d/autosaves/" t)))

(electric-pair-mode 1)

(use-package doom-modeline ;; required M-x nerd-icons-install-fonts
  :init (doom-modeline-mode 1))

(when (window-system)
  (set-frame-height (selected-frame) 33)
  (set-frame-width (selected-frame) 128))



;; --- Completion & UI stack ---

(use-package vertico
  :init
  (vertico-mode))

(use-package orderless
  :init
  (setq completion-styles '(orderless)
        completion-category-defaults nil
        completion-category-overrides
        '((file (styles partial-completion)))))  ;; for paths

(use-package marginalia
  :after vertico
  :init
  (marginalia-mode))

(use-package embark
  :bind
  (("C-." . embark-act)         ;; context menu
   ("C-;" . embark-dwim)        ;; smart default action
   ("C-h B" . embark-bindings)) ;; describe bindings
  :init
  (setq prefix-help-command #'embark-prefix-help-command))

(use-package consult
  :ensure t
  :bind (("C-x b" . consult-buffer)
         ("C-s" . consult-line)
         ("M-y" . consult-yank-pop)
         ("C-c h" . consult-history)
         ("C-c k" . consult-kmacro)
         ("C-c r" . consult-ripgrep)
         ("C-c f" . consult-find)
         ("C-M-l" . consult-imenu)))

(use-package embark-consult
  :after (embark consult)) ;; enrich consult via Embark

(use-package consult-projectile
  :ensure t
  :after (consult projectile)
  :bind (("C-c p f" . consult-projectile-find-file)
         ("C-c p p" . consult-projectile-switch-project)
         ("C-c p r" . consult-projectile-recentf)
         ("C-c p b" . consult-projectile-switch-to-buffer)))

(use-package which-key
  :init (which-key-mode))

(use-package treemacs
  :bind (("C-c t" . treemacs-select-window))
  :config (setq treemacs-is-never-other-window t))

(use-package treemacs-projectile
  :after (treemacs projectile))

(projectile-load-known-projects)

(use-package magit 
  :ensure t
  :pin melpa-stable
  :bind (("C-x g" . magit-status)))

(use-package auctex
  :defer t)

(defvar my/work-buffer nil
  "The special work buffer to jump to with `my/toggle-work-buffer'.")

(defun my/toggle-work-buffer (&optional set-new)
  "Toggle to the stored work buffer.
With prefix arg SET-NEW (C-u), set the current buffer as the new work buffer.
If the stored buffer no longer exists, reset it to the current buffer.
If already in the work buffer, bury it (toggle away)."
  (interactive "P")
  (cond
   ;; Explicitly set a new work buffer
   (set-new
    (setq my/work-buffer (current-buffer))
    (message "Work buffer set to: %s" (buffer-name my/work-buffer)))
   ;; If work buffer is dead or unset, reset to current
   ((not (and my/work-buffer (buffer-live-p my/work-buffer)))
    (setq my/work-buffer (current-buffer))
    (message "Work buffer was invalid, reset to: %s" (buffer-name my/work-buffer)))
   ;; If we're in the work buffer, bury it
   ((eq (current-buffer) my/work-buffer)
    (bury-buffer)
    (message "Buried work buffer: %s" (buffer-name my/work-buffer)))
   ;; Otherwise, jump to it
   (t
    (switch-to-buffer my/work-buffer)
    (message "Switched to work buffer: %s" (buffer-name my/work-buffer)))))

(global-set-key (kbd "C-c w") #'my/toggle-work-buffer)

(use-package vundo
  :ensure t
  :bind (("C-x u" . vundo)))

(use-package elpy
  :init (elpy-enable))

(use-package devdocs
  :ensure t
  :commands (devdocs-lookup devdocs-install)
  :bind (("C-c d" . devdocs-lookup)))
