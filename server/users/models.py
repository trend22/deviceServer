from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class MyUserManager(BaseUserManager):
    # Создаём метод для создания пользователя
    def _create_user(self, email, username, password, **extra_fields):
        '''Если нет почты, то прокидываем ошибку'''
        if not email:
            raise ValueError("email не был введён")

        '''Если нет логина, то прокидываем ошибку'''
        if not username:
            raise ValueError("username не был введён")

        # создаём пользователя
        '''normalize_email возвращает email c lowercase доменом'''
        user = self.model(
            email=self.normalize_email(email),
            username=username, **extra_fields,
        )

        #сохраняем пароль
        user.set_password(password)

        # Сохраняем всё остальное
        user.save(using=self._db)

        # Возвращаем пользователя
        return user

    # Делаем метод для создание обычного пользователя
    def create_user(self, email, username, password):
        # Возвращаем нового созданного пользователя
        return self._create_user(email, username, password)

    # Делаем метод для создание админа сайта
    def create_superuser(self, email, username, password):
        # Возвращаем нового созданного админа
        return self._create_user(email, username, password, is_staff=True, is_superuser=True)

    # Делаем метод для создание модератора сайта
    def create_staff(self, email, username, password):
        # Возвращаем нового созданного админа
        return self._create_user(email, username, password, is_staff=True, is_superuser=False)


'''создаём модель пользователя'''
class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True) # Идентификатор
    username = models.CharField(max_length=50, unique=True)  # Логин
    email = models.EmailField(max_length=100, unique=True)  # Email
    is_active = models.BooleanField(default=True)  # Статус активации
    is_staff = models.BooleanField(default=False)  # Статус админа

    USERNAME_FIELD = 'email'  # Идентификатор для обращения
    REQUIRED_FIELDS = ['username']  # Список имён полей для Superuser

    objects = MyUserManager()  # Добавляем методы класса MyUserManager

    # Метод для отображения в админ панели
    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'
