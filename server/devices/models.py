from django.db import models

from users.models import User

'''Определяем модели устройств(Device) и связанных с ними моделей'''


class ClassOfDevice(models.Model):
    name = models.CharField('Класс оборудования', max_length=256)

    # add name of class to admin page

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы оборудования'
        db_table = 'device_classes'


class CompanyUse(models.Model):
    name = models.CharField('Компания-эксплуатант', max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Эксплуатант'
        verbose_name_plural = 'Эксплуатанты'
        db_table = 'company_uses'


class Device(models.Model):
    name = models.CharField('Наименование', max_length=200)
    serial_number = models.CharField('Серийный номер', max_length=50)
    device_info = models.TextField('Дополнительная информация', max_length=10000, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default='admin', verbose_name='права')
    class_device = models.ForeignKey(ClassOfDevice, on_delete=models.SET_NULL, null=True,
                                     verbose_name='класс технического средства')
    who_use = models.ForeignKey(CompanyUse, on_delete=models.SET_NULL, null=True,
                                verbose_name='эксплуатант')

    def __str__(self):
        return self.name + ', ' + self.serial_number

    class Meta:
        verbose_name = 'Техническое средство'
        verbose_name_plural = 'Технические средства'
        db_table = 'devices'


'''Определяем модели проверок и связанных с ними моделей'''


class IntervalCheck(models.Model):
    interval = models.DecimalField('Интервал проверки, год', max_digits=3, decimal_places=1)

    # add name of Company to admin page CompanyCheck
    def __str__(self):
        return '{}'.format(self.interval)

    class Meta:
        verbose_name = 'Интервал'
        verbose_name_plural = 'Интервалы'
        db_table = 'interval_checks'


class CompanyCheck(models.Model):
    name = models.CharField('Компания-поверитель', max_length=256)

    # add name of Company to admin page CompanyCheck
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поверитель'
        verbose_name_plural = 'Поверители'
        db_table = 'company_checks'


class TypeOfSi(models.Model):
    name = models.CharField('Тип СИ', max_length=256)
    regNumber = models.CharField('Номер госреестра (ФИФ по ОЕИ)', max_length=10)
    interval = models.ForeignKey(IntervalCheck, on_delete=models.SET_NULL, null=True)

    # add name of Company to admin page Type of Si
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип СИ'
        verbose_name_plural = 'Типы СИ'
        db_table = 'type_of_sis'


'''Модель проверки средств измерений'''

'''добавляем related_name='si_checks',чтобы добавить SiCheck в модель Device. 
Смотреть сериализатор.DeviceWithSiCheckSerializer'''


class SiCheck(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, verbose_name='средство измерений',
                               related_name='si_checks')
    date_verify = models.DateField('Дата поверки', null=True)
    number_verify = models.CharField('Реквизит проверки', max_length=100, null=True)
    price_verify = models.DecimalField('Стоимость поверки', max_digits=10, decimal_places=2, null=True)
    type = models.ForeignKey(TypeOfSi, on_delete=models.SET_NULL, null=True, verbose_name='Тип СИ')
    who_check = models.ForeignKey(CompanyCheck, on_delete=models.SET_NULL, null=True,
                                  verbose_name='поверитель')

    def __str__(self):
        return self.device.name + ', ' + self.device.serial_number + ': ' + str(self.date_verify)

    class Meta:
        verbose_name = 'Поверка СИ'
        verbose_name_plural = 'Поверки СИ'
        db_table = 'si_checks'


'''Модель проверки испытательного оборудования'''


class IoCheck(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, verbose_name='испытательное оборудование',
                               related_name='io_checks')
    date_verify = models.DateField('Дата аттестации', null=True)
    number_attestation = models.CharField('Реквизит аттестации', max_length=100, null=True)
    is_first_attestation = models.BooleanField('Первичная аттестация', null=True, default=False)
    interval = models.ForeignKey(IntervalCheck, on_delete=models.SET_NULL, null=True,
                                 verbose_name='Интервал аттестации')
    who_check = models.ForeignKey(CompanyCheck, on_delete=models.SET_NULL, null=True,
                                  verbose_name='Аттестовщик')

    def __str__(self):
        return self.device.name + ', ' + self.device.serial_number + ': с ' + str(self.date_attestation) + \
               ' до ' + str(self.date_attestation)

    class Meta:
        verbose_name = 'Аттестация ИО'
        verbose_name_plural = 'Аттестация ИО'
        db_table = 'io_checks'


'''Модель проверки индикаторов'''


class IndicatorCheck(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, verbose_name='индикаторы',
                               related_name='indicator_checks')
    date_verify = models.DateField('Дата проверки', null=True)
    number_check = models.CharField('Реквизит проверки', max_length=100, null=True)
    interval = models.ForeignKey(IntervalCheck, on_delete=models.SET_NULL, null=True, verbose_name='Интервал проверки')
    who_check = models.ForeignKey(CompanyCheck, on_delete=models.SET_NULL, null=True,
                                  verbose_name='Проверяющая организация')

    def __str__(self):
        return self.device.name + ', ' + self.device.serial_number + ': ' + str(self.date_check)

    class Meta:
        verbose_name = 'Проверка индикатора'
        verbose_name_plural = 'Проверки индикаторов'
        db_table = 'indicator_checks'


'''Модель проверки средств контроля'''


class SkCheck(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, verbose_name='средства контроля',
                               related_name='sk_checks')
    date_verify = models.DateField('Дата проверки', null=True)
    number_check = models.CharField('Реквизит проверки', max_length=100, null=True)
    docs = models.TextField('Информация о документации (методики, ЭД)', max_length=10000, null=True)
    interval = models.ForeignKey(IntervalCheck, on_delete=models.SET_NULL, null=True, verbose_name='Интервал проверки')
    who_check = models.ForeignKey(CompanyCheck, on_delete=models.SET_NULL, null=True,
                                  verbose_name='Проверяющая организация')

    def __str__(self):
        return self.device.name + ', ' + self.device.serial_number + ': ' + str(self.date_check)

    class Meta:
        verbose_name = 'Проверка средства контроля'
        verbose_name_plural = 'Проверки средств контроля'
        db_table = 'sk_checks'
