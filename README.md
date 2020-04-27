# django utilities
check_ldap.py can be used as django command to check LDAP authentification of users stored in Django's database.

This command requires ldap3 and  django-python3-ldap 

usage: manage.py check_ldap [-h] -u USER -p PASSWORD 
Checks the existence of the user locally and his authentication via the LDAP
server

required arguments:
-u USER, --user USERNAME
-p PASSWORD, --password PASSWORD
--------------------------------------------------------

optional arguments:
  -h, --help            show this help message and exit
