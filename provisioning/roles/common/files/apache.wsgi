import os

# TODO
activate_this = os.path.join('/usr/lib/ckan/default/bin/activate_this.py')

# TODO
execfile(activate_this, dict(__file__=activate_this))

print("In Apache WSGI script.")

from paste.deploy import loadapp

#
config_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'production.ini')
#
from paste.script.util.logging_config import fileConfig
#
fileConfig(config_filepath)
#
application = loadapp('config:%s' % config_filepath)