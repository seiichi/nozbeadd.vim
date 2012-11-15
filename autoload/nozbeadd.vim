" nozbeadd.vim - Vim plugin to add a action to Nozbe within Vim
"
" Author: Seiichi SATO <seiichisato@gmail.com>
" License: http://www.opensource.org/licenses/bsd-license.php

func! nozbeadd#addAction(...)
  python Nozbe.getInstance().addAction()
endf

if has('python')
python << EOF
import sys, os, vim
sys.path.append(os.path.join(vim.eval('expand("<sfile>:p:h")'), '../plugin/py/'))
from nozbe import Nozbe
EOF
endif
