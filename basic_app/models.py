from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    '''
    This is a class that add additional information to the default User model,
    which already contains USERNAME, EMAIL, PASSWORD, FISTNAME and SURNAME
    '''
    # The reason that make this one-to-one map instead of inherit is that the
    # latter may create multiple instances to one user
    user = models.OneToOneField(User)

    # additional
    portfolio_site = models.URLField(blank=True)
    # blank=True means user does not have to fill in that specfic field
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return "{}".format(self.user.username)
