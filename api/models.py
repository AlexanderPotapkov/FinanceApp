from django.contrib.auth import password_validation
from django.db import models
from django.contrib.auth.models import AbstractUser

"""
    Используем встроенную модель User
"""


class User(AbstractUser):

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        Categories.objects.create(categoryName='Зарплата', user=self, category_type='CC')
        Categories.objects.create(categoryName='Подработка', user=self, category_type='CC')
        Categories.objects.create(categoryName='Пассивный доход', user=self, category_type='CC')
        Categories.objects.create(categoryName='Подработка', user=self, category_type='OC')
        Categories.objects.create(categoryName='Наследство', user=self, category_type='OC')
        if self._password is not None:
            password_validation.password_changed(self._password, self)
            self._password = None

class Categories(models.Model):
    constant_cat = 'CC'
    once_cat = 'OC'
    CAT_TYPES = [
        (constant_cat, 'Постоянные'),
        (once_cat, 'Разовые'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    categoryName = models.CharField(max_length=255, default="Название категории", verbose_name='Название категории')
    category_type = models.CharField(max_length=2, choices=CAT_TYPES, default=constant_cat)

    def __str__(self):
        return self.categoryName


class AbstractCash(models.Model):
    class Meta:
        abstract = True

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    reg_sum = models.IntegerField(verbose_name='Постоянная сумма')
    var_sum = models.IntegerField(verbose_name='Переменная сумма')
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Категория', null=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')


class OutcomeCash(AbstractCash):
    pass


class IncomeCash(AbstractCash):
    pass


class MoneyBox(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    box_name = models.CharField(max_length=255, verbose_name='Название копилки')
    box_sum = models.IntegerField(verbose_name='Сумма в копилке')
