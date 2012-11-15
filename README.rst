============
nozbeadd.vim
============

About
-----

nozbeadd.vim is a utility plugin which allows you to add new actions to your
inbox of Nozbe_ within Vim.

.. _Nozbe: http://www.nozbe.com/

Requirements
------------

* Python
* Vim compiled with python support

Installation
------------

If you use Vundle_, add to your ``.vimrc``::

    Bundle 'seiichi/nozbeadd.vim'
    let g:nozbe_api_key = "YOUR NOZBE API KEY"

.. _Vundle: https://github.com/gmarik/vundle

Usage
-----

Run ``:NozbeAdd`` as below::

    :NozbeAdd NEW ACTION

Author
------

Seiichi SATO <seiichisato@gmail.com>

