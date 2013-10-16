;;; helpers for writing blogs with tinkerer

(require 'dash)


(defvar my-blog-root "~/Documents/blog"
  "The root directory of your blog")


(defun tinker (tail &optional buffer)
  (let ((cmd (format "cd %s && tinker %s" my-blog-root tail)))
    (message (format "Running: %s" cmd))
    (if buffer
	(shell-command cmd  buffer)
      (shell-command cmd))))


(defun my-blog-create-new-draft (title)
  (with-temp-buffer
    (tinker (format "-d %s" title))
    (goto-char 0)
    (buffer-substring (search-forward "'") (- (search-forward "'") 1))))


(defun my-blog-new-draft ()
  (interactive)
  (let ((title (read-from-minibuffer "Title? ")))
    (find-file (my-blog-create-new-draft title))))


(defun my-blog-preview-draft ()
  (interactive)
  (with-temp-buffer
    (tinker (format "--preview %s" (buffer-file-name))))
  (let ((blog-index (concat (expand-file-name my-blog-root) "/blog/html/index.html")))
    (find-file blog-index)
    (browse-url-of-file)))


(defun my-blog-rst-files ()
  (with-temp-buffer
    (shell-command
     (concat "find " my-blog-root " -name '*.rst' | grep -v '_templates' | sort -r")
     (current-buffer))
    (let ((blog-files (split-string (buffer-string) "\n")))
      (-zip blog-files blog-files))))


(defun my-blog-open-file (fn)
  (find-file fn))

(defun helm-source-my-blog
  '((name . "My Blog Files!")
    (candidates . my-blog-rst-files)
    (action . (("Do something" . my-blog-open-file)))))



(defun my-blog-find-files ()
  (interactive)
  (helm :sources '(helm-source-my-blog)))

(provide 'my-blog)
