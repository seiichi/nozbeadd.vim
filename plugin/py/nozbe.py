# Author: Seiichi SATO <seiichisato@gmail.com>
# License: http://www.opensource.org/licenses/bsd-license.php

_BASE_URL = 'https://webapp.nozbe.com/api'

import vim
import urllib
import urllib2
import json

class Nozbe(object):
    _instance = None

    def __init__(self):
        if Nozbe._instance is not None:
            raise RuntimeError('BUG: Nozbe.__init__()')

    @classmethod
    def getInstance(self):
        if Nozbe._instance is None:
            Nozbe._instance = Nozbe()
            Nozbe._instance._key = vim.eval('g:nozbe_api_key')

        return Nozbe._instance

    def _err(self, msg):
        vim.command("echoerr 'nozbe: %s'" % (msg))

    def addAction(self):
        name = urllib.quote(vim.eval('a:1'))
        key = self._key
        url = '%s/newaction/name-%s/what-next/key-%s' % (_BASE_URL, name, key)

        try:
            vim.command("echo 'sending new action...'")
            u = urllib2.urlopen(url)
            json.loads(u.read())
            vim.command("redraw")
            vim.command("echo 'done'")
        except urllib2.URLError, e:
            self._err("failed to access the server [%s]" % (e))
        except ValueError, e:
            self._err("failed to add new action [%s]'" % (e))
