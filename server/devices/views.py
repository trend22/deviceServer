from django_filters.rest_framework import DjangoFilterBackend
from drf_multiple_model.views import FlatMultipleModelAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from .models import Device, CompanyUse, ClassOfDevice, SiCheck, IoCheck, IndicatorCheck, SkCheck, IntervalCheck, \
    CompanyCheck, TypeOfSi
from .permissions import IsStaffOnlyOrReadAny
from .serializers import DeviceSerializer, CompanyUseSerializer, ClassOfDeviceSerializer, SiCheckSerializer, \
    IoCheckSerializer, IndicatorCheckSerializer, SkCheckSerializer, IntervalCheckSerializer, CompanyCheckSerializer, \
    TypeOfSiSerializer

'''Представления для моделей устройств'''


class DeviceViewSet(ModelViewSet):
    # get all company uses
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsStaffOnlyOrReadAny]


class CompanyUseViewSet(ModelViewSet):
    # get all company uses
    queryset = CompanyUse.objects.all()
    serializer_class = CompanyUseSerializer
    permission_classes = [IsStaffOnlyOrReadAny]


class ClassOfDeviceViewSet(ModelViewSet):
    # get all company checks
    queryset = ClassOfDevice.objects.all()
    serializer_class = ClassOfDeviceSerializer
    '''Для проверки аутентификации пользователя при запросах - IsAuthenticated'''
    '''IsAuthenticatedOrReadOnly - Get запросы доступны для обычных юзеров'''
    permission_classes = [IsStaffOnlyOrReadAny]
    '''подключение фильтров'''
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_field = ['name']


'''представления для моделей проверок'''


class SiCheckViewSet(ModelViewSet):
    # get all company uses
    queryset = SiCheck.objects.all()
    serializer_class = SiCheckSerializer
    permission_classes = [IsStaffOnlyOrReadAny]


class IoCheckViewSet(ModelViewSet):
    # get all company uses
    queryset = IoCheck.objects.all()
    serializer_class = IoCheckSerializer
    permission_classes = [IsStaffOnlyOrReadAny]


class IndicatorCheckViewSet(ModelViewSet):
    # get all company uses
    queryset = IndicatorCheck.objects.all()
    serializer_class = IndicatorCheckSerializer
    permission_classes = [IsStaffOnlyOrReadAny]


class SkCheckViewSet(ModelViewSet):
    # get all company uses
    queryset = SkCheck.objects.all()
    serializer_class = SkCheckSerializer
    permission_classes = [IsStaffOnlyOrReadAny]


class AllCheckAPIView(FlatMultipleModelAPIView):
    pagination_class = None
    querylist = [
        {'queryset': SiCheck.objects.all(), 'serializer_class': SiCheckSerializer},
        {'queryset': IoCheck.objects.all(), 'serializer_class': IoCheckSerializer},
        {'queryset': IndicatorCheck.objects.all(), 'serializer_class': IndicatorCheckSerializer},
        {'queryset': SkCheck.objects.all(), 'serializer_class': SkCheckSerializer},
    ]


class IntervalCheckViewSet(ModelViewSet):
    # get all company checks
    queryset = IntervalCheck.objects.all()
    serializer_class = IntervalCheckSerializer
    '''Для проверки аутентификации пользователя при запросах - IsAuthenticated'''
    '''IsAuthenticatedOrReadOnly - Get запросы доступны для незарегистрированных юзеров'''
    permission_classes = [IsStaffOnlyOrReadAny]
    '''подключение фильтров'''
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['interval']
    search_fields = ['interval']
    ordering_field = ['interval']


class CompanyCheckViewSet(ModelViewSet):
    # get all company checks
    queryset = CompanyCheck.objects.all()
    serializer_class = CompanyCheckSerializer
    '''Для проверки аутентификации пользователя при запросах - IsAuthenticated'''
    '''IsAuthenticatedOrReadOnly - Get запросы доступны для незарегистрированных юзеров'''
    permission_classes = [IsStaffOnlyOrReadAny]
    '''подключение фильтров'''
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_field = ['name']


class TypeOfSiViewSet(ModelViewSet):
    # get all company checks
    queryset = TypeOfSi.objects.all()
    serializer_class = TypeOfSiSerializer
    '''Для проверки аутентификации пользователя при запросах - IsAuthenticated'''
    '''IsAuthenticatedOrReadOnly - Get запросы доступны для незарегистрированных юзеров'''
    permission_classes = [IsStaffOnlyOrReadAny]
    '''подключение фильтров'''
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'regNumber']
    search_fields = ['name', 'regNumber']
    ordering_field = ['name', 'regNumber']
