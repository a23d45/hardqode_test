from django.db import models

from accounts.models import User


class Product(models.Model):
    """Модель продукта"""
    name = models.CharField(
        verbose_name='Название',
        max_length=30,
        unique=True
    )
    author = models.ForeignKey(
        verbose_name = 'Преподаватель',
        to=User,
        on_delete=models.CASCADE,
        related_name='created_products'
    )
    price = models.DecimalField(
        verbose_name='Стоимость',
        max_digits=10, 
        decimal_places=2
    )
    start_date_time = models.DateTimeField(
        verbose_name='Старт',
        auto_now_add=True
    )
    students = models.ManyToManyField(
        verbose_name='Ученики',
        to=User,
        related_name='available_products',
    )

    min_number_users_in_group = models.PositiveIntegerField(
        verbose_name='Минимальный размер группы',
        default=2
    )

    max_number_users_in_group = models.PositiveIntegerField(
        verbose_name='Максимальный размер группы',
        default=5
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Lesson(models.Model):
    """Модель урока"""
    name = models.CharField(
        verbose_name='Название',
        max_length=40
    )
    product = models.ForeignKey(
        verbose_name='Продукт',
        to=Product,
        on_delete=models.CASCADE,
        related_name='lessons'
    )
    link = models.URLField(
        verbose_name='Ссылка на урок',
        unique=True
    )

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    
class Group(models.Model):
    """Модель группы пользователей"""
    name = models.CharField(
        verbose_name='Название',
        max_length=30
    )
    product = models.ForeignKey(
        verbose_name='Продукт',
        to=Product,
        on_delete=models.CASCADE,
        related_name='groups'
    )
    students = models.ManyToManyField(
        verbose_name='Ученики',
        to=User,
        related_name='product_groups',
    )
