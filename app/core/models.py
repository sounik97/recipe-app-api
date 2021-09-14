from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,\
                                        PermissionsMixin

'''
The Usermanager class helps django to make user using existing imported models
'''
class UserManager (BaseUserManager):

    def create_user(self, email, password= None, **extra_fields):
        '''
        **extra_fields means take any extra parameters availableself.

        normalize_email funcation helps in the case sensitive part
        '''

        ''' This function create and save new user'''

        if not email:
            raise ValueError('Users Must Have an email address')

        user = self.model(email = self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self, email, password):
        ''' creates and saves new superuser '''

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True

        user.save(using = self._db)

        return user

class User( AbstractBaseUser, PermissionsMixin):
    ''' Custom user model that supports using email instead username'''
    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default = False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
