#!/Users/caoguangyao/heroku-trac/venv/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C)2008-2009 Edgewall Software
# Copyright (C) 2008 Noah Kantrowitz <noah@coderanger.net>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution. The terms
# are also available at http://trac.edgewall.org/wiki/TracLicense.
#
# This software consists of voluntary contributions made by many
# individuals. For the exact contribution history, see the revision
# history and logs, available at http://trac.edgewall.org/log/.
#
# Author: Noah Kantrowitz <noah@coderanger.net>
import sys
import os

sys.stdout = sys.stderr
APP_ROOT = os.path.dirname(__file__)
#put here your ENV's Variables
# here is an example with multiple instances
os.environ['TRAC_ENV_PARENT_DIR'] = APP_ROOT#os.path.join(APP_ROOT,'myproject') 
os.environ['PYTHON_EGG_CACHE'] = os.path.join(APP_ROOT,'myproject/.eggs/') 

import trac.web.main
application = trac.web.main.dispatch_request

