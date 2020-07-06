from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, Group)
from django.utils import timezone
from django.db import models
from .managers import UserManager
from softdelete.models import SoftDeleteObject


class User(AbstractBaseUser, SoftDeleteObject, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=50, null=True)
    groups = models.ForeignKey(
        to=Group,
        on_delete=models.CASCADE,
        null=True
        )
    date_of_birth = models.DateField(blank=True, null=True)
    picture = models.ImageField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['groups']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    class Meta:
        permissions = [
            ("can_create_admin_users", "Can create users with group Admin"),
            ("can_list_all_users", "Can list all users"),
        ]




"""
    En caso de habilitar registración por el Usuario descomentar
"""
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def _post_save_receiver(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
