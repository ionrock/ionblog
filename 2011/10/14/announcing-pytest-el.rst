Announcing Pytest.el
####################

The other day when I rebooted my Emacs set up to use the ELPA and
Marmalade repos, I took a little time to see what other packages were
out there that might be interesting. I found Nosemacs which seemed
pretty slick and took a look. My experiments with Nose having failed for
the time being, I looked at porting it to use pytest.
The result is pytest.el and it is available in the Marmalade repo.
The functionality is pretty much the same as Nosemacs. When you open a
test file you can run the entire "module" (the file) with the
pytest-module function. You can also run the test your cursor is in with
pytest-one. To test all the files in the directory of the current
buffer, use pytest-directory. Finally, you can use pytest-all to run the
entire test suite.
Since I use virtualenv for many projects, I end up wanting to use my
virtualenv's version of pytest. Pytest.el supports this by allowing you
to configure what test runner you want to use. You can read more about
this in the actual code.
Here is what I currently have in my .emacs:

    ::

        ;; py.test

        (load-file "~/Projects/pytest-el/pytest.el")

        (require 'pytest)

        (add-to-list 'pytest-project-names "run-tests")

        (setq pytest-use-verbose nil) ; non-verbose output

        (setq pytest-loop-on-failing nil) ; don't use the -f flag from xdist

        (setq pytest-assert-plain t) ; don't worry about re-evaluating exceptions (faster)



        ;; python-mode hook

        (defun my-python-mode-hook ()

           (linum-mode t) ; show line numbers

           (subword-mode t) ; allow M-b to understand camel case

           (setq tab-width 4) ; pep8

           (local-set-key (kbd "C-c a") 'pytest-all)

           (local-set-key (kbd "C-c m") 'pytest-module)

           (local-set-key (kbd "C-c .") 'pytest-one)

           (local-set-key (kbd "C-c d") 'pytest-directory)

           (setq indent-tabs-mode nil))

        (add-hook 'python-mode-hook 'my-python-mode-hook)

This is my first Emacs package, so any suggestions are welcome on how
to improve things. I'd like to eventually make the configuration
variables customizable via customize.


.. author:: default
.. categories:: code
.. tags:: emacs, programming, python, testing
.. comments::
