" nozbeadd.vim - Vim plugin to add a action to Nozbe within Vim
"
" Author: Seiichi SATO <seiichisato@gmail.com>
" License: http://www.opensource.org/licenses/bsd-license.php

if !has('python')
  echo "nozbeadd plugin requires python"
  finish
endif

if !exists('g:nozbe_api_key')
  let g:nozbe_api_key = ''
endif

com! -nargs=1 NozbeAdd call nozbeadd#addAction(<q-args>)
