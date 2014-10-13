import os, pickle

settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))

def readenvfile(filename):
    if not os.path.exists(filename):
        raise IOError("file {} not found".format(filename))

    command = 'export $(cat {}|grep -v -e "^#"|xargs)'.format(filename)
    dump = '/usr/bin/python -c "import os,pickle;print pickle.dumps(os.environ)"'
    penv = os.popen('%s && %s' %(command,dump))
    env = pickle.loads(penv.read())
    os.environ = env

from django.core.exceptions import ImproperlyConfigured
try:
    filename = "{}/{}".format(PROJECT_ROOT, os.environ.get('CABOT_CONFIG'))
    print filename
    readenvfile(filename)
except IOError:
    raise ImproperlyConfigured('No configuration file present.')

