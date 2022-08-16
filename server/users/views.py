# Подключаем статус
from django.middleware.csrf import RejectRequest, InvalidTokenFormat
from rest_framework import status
# Подключаем компонент для ответа
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
# Подключаем компонент для создания данных
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
# Подключаем компонент для прав доступа
from rest_framework.permissions import AllowAny, IsAdminUser
# Подключаем модель User
from rest_framework.viewsets import ModelViewSet

from .models import User
# Подключаем UserRegistrSerializer
from .serializers import UserRegistrSerializer, UsersSerializer, DeletePutPatchUserSerializer


# Создаём класс RegistrUserView
class RegistrUserView(CreateAPIView):
    # Добавляем в queryset
    queryset = User.objects.all()
    # Добавляем serializer UserRegistrSerializer
    serializer_class = UserRegistrSerializer
    # Добавляем права доступа
    permission_classes = [AllowAny]

    # Создаём метод для создания нового пользователя
    def post(self, request, *args, **kwargs):
        # Добавляем UserRegistrSerializer
        serializer = UserRegistrSerializer(data=request.data)
        # Создаём список data
        data = {}

        # Проверка данных на валидность
        if serializer.is_valid():
            # Сохраняем нового пользователя
            serializer.save()
            # Добавляем в список значение ответа True
            data['response'] = True
            # Возвращаем что всё в порядке
            return Response(data, status=status.HTTP_200_OK)
        else:  # Иначе
            # Присваиваем data ошибку
            data = serializer.errors
            # Возвращаем ошибку
            return Response(data)


# создаём класс для запросов, изменений и удалений пользователей
class AllUsersView(ListAPIView):
    # Получаем набор всех записей из таблицы Capital
    queryset = User.objects.all()
    # Сериализуем извлечённый набор записей
    serializer_class = UsersSerializer

    permission_classes = [IsAdminUser]


# создаём класс для DELETE, PUT, PATCH и RETRIEVE для админа
class DeletePutPatchUserView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    # Добавляем serializer UserRegistrSerializer
    serializer_class = DeletePutPatchUserSerializer
    # переопределяем поле, по которому находим юзера в urls
    lookup_field = 'id'
    # Добавляем права доступа
    permission_classes = [IsAdminUser]




