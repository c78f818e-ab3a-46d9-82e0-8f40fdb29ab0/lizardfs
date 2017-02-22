#!/usr/bin/python

import sys
import socket

try:
    import collectd
except ImportError:
    pass

try:
    import moosefs
except ImportError:
    print '\nError al importar moosefs, verificar instalacion\n'
    sys.exit(2)

master = ''
port = 9421


