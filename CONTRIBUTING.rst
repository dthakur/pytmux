How to Contribute
=================

All development is done via GitHub using issues and pull requests. If you are
doing something major (new feature, backwards incompatible change, reworking
lots of code) please open an issue and discuss it before starting. If you are
doing something minor (docs update, small bug fix, etc) feel free to just dive
in and send a pull request.

Code Standards
--------------

All code should pass ``pep8`` and ``pyflakes``. A simple tool for checking is
`flake8 <https://pypi.python.org/pypi/flake8>`_. You should be able to run::

  flake8 .

At the root of the repository and have 0 errors or warnings. That said,
everyone slips now and then, and one or two isn't a big deal and I'll just fix
them myself. But if your whole patch fails then I'll likely reject it until you
clean up your code.

Reporting Issues
----------------

You can report issues and feature via the `issue tracker
<https://github.com/wraithan/pytmux/issues>`_. If you have an issue please give
full steps to reproduce (such as a config file that has the problem). If you
have a feature you'd like, please provide as much information as possible (such
as what flags in tmux the feature uses or how exactly you'd like it to work.)
