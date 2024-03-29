from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Модель пользователя"""
    ROLES = (
        (False, 'Ученик'),
        (True, 'Преподаватель')
    )
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. \
                Letters, digits and @/./+/-/_ only.'
        ),
        validators=[
            AbstractUser.username_validator,
            RegexValidator('^[^@]*$')  # строка любой длины, не содержащая @
        ],
        error_messages={
            'unique': _('A user with that username already exists.'),
        },
    )
    role = models.BooleanField(
        verbose_name='Роль',
        choices=ROLES
    )
