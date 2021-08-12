import datetime

from django.utils.timezone import now

from django.db import models

from goods.models import OrganizationProduct, Product
from organizations import enums


class Organizations(models.Model):
    """
    Defining whole information about audience organization
    """
    brand = models.CharField(verbose_name='نام سازمان', max_length=200)
    landline = models.IntegerField(verbose_name='تلفن سازمان', default=0)
    state = models.CharField(verbose_name='استان', max_length=50)
    workers = models.IntegerField(verbose_name='تعداد کارگران', default=1)
    fullname_audience = models.CharField(verbose_name='نام و نام خانوادگی مخاطب', max_length=150)
    date_registration = models.DateField(verbose_name='تاریخ ثبت', auto_now_add=True)
    registrar = models.ForeignKey('auth.User', verbose_name='کارشناس ثبت کننده', on_delete=models.PROTECT)
    products = models.ManyToManyField('goods.OrganizationProduct', verbose_name='محصولات تولیدی')
    phone_number = models.IntegerField(verbose_name='شماره تلفن مخاطب', null=True, blank=True)
    email = models.EmailField(verbose_name='آدرس پست الکترونیکی', max_length=155)

    class Meta:
        verbose_name = 'سازمان'
        verbose_name_plural = 'سازمان ها'
        unique_together = ['brand', 'registrar']

    def organizations_info_products(self):
        """
        Appends all of the products of the organization into a list
        """
        product_list = list()
        for product in self.products.all():
            product_list.append(product)
        return product_list

    def __str__(self):
        return f'{self.brand}'


class EmailHistory(models.Model):
    """
    Send an email and Save its status, date, sender and receiver
    """
    sender = models.CharField(verbose_name='ارسال کننده', max_length=100)
    receiver = models.CharField(verbose_name='دریافت کننده', max_length=100)
    sends_on = models.DateTimeField(verbose_name='تاریخ ارسال', auto_now_add=True)
    status = models.CharField(verbose_name='وضعیت', help_text='وضعیت ارسال', choices=enums.EmailStatuses.choices,
                              max_length=100)

    class Meta:
        verbose_name = 'تاریخچه ایمیل'
        verbose_name_plural = 'تاریخچه ایمیل ها'

    def __str__(self):
        return f'سازمان {self.receiver}'
