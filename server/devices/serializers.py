from rest_framework.serializers import ModelSerializer

from .models import Device, CompanyUse, ClassOfDevice, SiCheck, IoCheck, IndicatorCheck, SkCheck, CompanyCheck, \
    IntervalCheck, TypeOfSi

'''Serializers для моделей устройства'''


class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class CompanyUseSerializer(ModelSerializer):
    class Meta:
        model = CompanyUse
        fields = '__all__'


class ClassOfDeviceSerializer(ModelSerializer):
    class Meta:
        model = ClassOfDevice
        fields = '__all__'


'''Serializers для моделей проверки'''


class SiCheckSerializer(ModelSerializer):
    class Meta:
        model = SiCheck
        fields = '__all__'


class IoCheckSerializer(ModelSerializer):
    class Meta:
        model = IoCheck
        fields = '__all__'


class IndicatorCheckSerializer(ModelSerializer):
    class Meta:
        model = IndicatorCheck
        fields = '__all__'


class SkCheckSerializer(ModelSerializer):
    class Meta:
        model = SkCheck
        fields = '__all__'

# create serializer for work with DB
class CompanyCheckSerializer(ModelSerializer):
    class Meta:
        # create model of serializer
        model = CompanyCheck
        # add all fields of CompanyCheck to serializer
        fields = '__all__'


# create serializer for work with DB
class IntervalCheckSerializer(ModelSerializer):
    class Meta:
        # create model of serializer
        model = IntervalCheck
        # add all fields of CompanyCheck to serializer
        fields = '__all__'


# create serializer for work with DB
class TypeOfSiSerializer(ModelSerializer):
    class Meta:
        # create model of serializer
        model = TypeOfSi
        # add all fields of CompanyCheck to serializer
        fields = '__all__'
