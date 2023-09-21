from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
import ldap3 
from ldap3.core.exceptions import LDAPException
from django_python3_ldap.conf import settings
import logging
#Check ldap User authentication
class Command(BaseCommand):

    help =  "Checks the existence of the django user (stored in a Django database) and his authentication via the LDAP server"
    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument('-u', '--user', type=str, help='Define a username', )
        parser.add_argument('-p', '--password', type=str, help='Define a password', )

    @transaction.atomic()
    def handle(self, *args, **kwargs):
        passd = kwargs["password"]
        User = get_user_model()
        username=kwargs["user"]

        try:
            user = User.objects.get(username=username)
            cn=user.get_full_name()
            cn="cn=" +cn + "," + settings.LDAP_AUTH_SEARCH_BASE
            self.stdout.write('cn={}'.format(cn))
        except User.DoesNotExist:
                raise CommandError("User with username {username} does not exist".format(
                    username=username,
                ))
        try:
            server= ldap3.Server(
                settings.LDAP_AUTH_URL,
                allowed_referral_hosts=[("*", True)],
                get_info=ldap3.NONE,
                connect_timeout=settings.LDAP_AUTH_CONNECT_TIMEOUT,
            )
            # Open a new connection to remote LDAP Server and bind the user
            c = ldap3.Connection(server,cn,passd,auto_bind=True)
            self.stdout.write("Successful LDAP login with user {} ".format(user));
            c.unbind()
        except ldap3.core.exceptions.LDAPExceptionError as exc:
           self.stdout.write('Failed to authenticate user ' + username + ' using LDAP: {}.'.format(str(exc)))  


