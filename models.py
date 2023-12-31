from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model


User = get_user_model()

class Advertisements(models.Model):
    title = models.CharField('заголовок', max_length=100)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('торг', help_text='Возможен торг или нет')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    image = models.ImageField("изображения", upload_to="advertisements/")

    @admin.display(description='дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='дата обновления')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: azure; font-weight: bold;">Сегодня в {}</span>', updated_time
            )
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")


class Meta:
    db_table = 'advertisements'

def _str_(self) -> str:
    return f"Advertisements(id = {self.id}, title = {self.title}, price = {self.price})"

