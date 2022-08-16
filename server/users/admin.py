from django.contrib import admin
from django.utils.translation import gettext_lazy

from users.models import User


# изменяем представление User в панели админ
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email')


# User - включаем отображение в админке, UserAdmin - изменяем отображение User в админке
admin.site.register(User, UserAdmin)


# изменяем в админ панели стандартные надписи
admin.site.site_header = gettext_lazy('Панель администратора сайта')
admin.site.site_index = gettext_lazy('Данные сайта')
