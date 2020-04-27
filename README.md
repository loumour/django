# django utilities
check_ldap.py can be used as django command to check LDAP authentification of users stored in Django's database.
This command requires ldap3 and  django-python3-ldap 

usage: manage.py check_ldap [-h] [-u USER] [-p PASSWORD] [--version]
                            [-v {0,1,2,3}] [--settings SETTINGS]
                            [--pythonpath PYTHONPATH] [--traceback]
                            [--no-color] [--force-color] [--skip-checks]

Checks the existence of the user locally and his authentication via the LDAP
server

optional arguments:
  -h, --help            show this help message and exit
  -u USER, --user USER  Define a username
  -p PASSWORD, --password PASSWORD
                        Define a password
  --version             show program's version number and exit
  -v {0,1,2,3}, --verbosity {0,1,2,3}
                        Verbosity level; 0=minimal output, 1=normal output,
                        2=verbose output, 3=very verbose output
  --settings SETTINGS   The Python path to a settings module, e.g.
                        "myproject.settings.main". If this isn't provided, the
                        DJANGO_SETTINGS_MODULE environment variable will be
                        used.
  --pythonpath PYTHONPATH
                        A directory to add to the Python path, e.g.
                        "/home/djangoprojects/myproject".
  --traceback           Raise on CommandError exceptions
  --no-color            Don't colorize the command output.
  --force-color         Force colorization of the command output.
  --skip-checks         Skip system checks.
